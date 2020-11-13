import ssl
from urllib.parse import urljoin, urlparse
import traceback, sys
from bs4 import BeautifulSoup
import socket

from .signal_sender import SignalSender
from main_window.main_widget.signals.prograss_bar_signal import PrograssBarSignalSender
from main_window.main_widget.signals.label_process_signal import LabelProcessSignalSender
from PySide2.QtCore import Slot, QRunnable


class LinkWorker(QRunnable):
    """
    Thread (Worker) to find information from certain urls
    Using socket (in most cases ssl - which work with HTTPS)

    """

    REQUEST_SIZE_TO_READ = 4096

    def __init__(
            self,
            address: str,
            port: int,
            depth: int,
            max_number_addresses: int,
            progress_bar_sender: PrograssBarSignalSender,
            label_process_sender: LabelProcessSignalSender
    ):
        super(LinkWorker, self).__init__()
        # Store images from main page
        self.main_images_set = set()
        # Store images from secondary sites
        self.second_images_set = set()

        self.address = address
        self.port = port
        self.depth = depth
        self.max_number_addresses = max_number_addresses
        self.all_urls = set()
        # Keep signal sender, to update progress bar
        self.progress_bar_sender = progress_bar_sender
        self.label_process_sender = label_process_sender
        # Sender for emit final result
        self.signals = SignalSender()

    @Slot()
    def run(self):
        try:
            # Extract images which are located on other sites
            urls = self.__get_urls_from_address_socket(self.address)

            self.main_images_set = self.__extract_img_from_other_sites_socket(self.address)
            self.second_images_set = self.__extract_img_from_other_sites_socket(urls)

        except ValueError as ex:
            self.signals.error.emit(f"Exception: {ex}\nBad url! {self.address}")

        except Exception as ex:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(self)  # Return the result of the processing
        finally:
            self.signals.finished.emit()    # Done

    def __separe_path_and_address(self, url):
        """
        Return two indexes:
            first - index at which main url starts (for example ssau.ru)
            second - index at which path starts (for example /news), if there is no path, return -1

        """
        first_ind = -1
        second_ind = -1

        for i in range(len(url)):
            if url[i] == '/':
                # Scip two // slesh
                first_ind = i + 2
                break

        for i in range(first_ind, len(url)):
            if url[i] == '/':
                second_ind = i
                break

        return first_ind, second_ind

    def __get_urls_from_address_socket(self, address, current_depth=0) -> list:
        """
        Return list of lists urls found at certain address

        """
        try:
            soup = BeautifulSoup(self.__extract_html(address), "html.parser")

            if soup is None:
                raise ValueError(f"Wrong url {address}")
            self.all_urls.add(address)
            # Store all found urls
            urls = [[]]
            # Search every urls and save it
            for a_tag in soup.findAll("a"):
                href = a_tag.attrs.get("href")
                if href == "" or href is None:
                    # href empty tag
                    continue
                # Join urls
                # for example self.adress = https://ssau.ru/, href = news, final output = https://ssau.ru/news
                if self.address not in href:
                    href = urljoin(self.address, href)
                parsed_href = urlparse(href)
                # remove URL GET parameters, URL fragments, etc.
                href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
                # Skip href if its already in `urls` or equal to input address
                if href in urls[0] or href in self.all_urls:
                    continue
                urls[0].append(href)
                self.all_urls.add(href)
                if len(urls[0]) >= self.max_number_addresses:
                    break

            if current_depth < self.depth:
                for single_url in urls[0]:
                    self.label_process_sender.whatProcess.emit(single_url)
                    urls.append(self.__get_urls_from_address_socket(single_url, current_depth=current_depth+1))

            return urls

        except Exception as ex:
            self.signals.error.emit(f"Exception: {ex}\nBad url! {address}")
            return []

    def __extract_img_from_other_sites_socket(self, addresses) -> set:
        """
        Extract images which are located on other sites
        And return list of these images

        """
        all_img_set = set()
        if isinstance(addresses, list):
            self.progress_bar_sender.maximum.emit(min(self.max_number_addresses, len(addresses)))
            for i, single_url_list in enumerate(addresses):
                # Get list of all urls
                all_urls_from_single_url = self.__get_all_urls_from_list(single_url_list)
                # On every url find images and save into list
                for m, single_url_depth in enumerate(all_urls_from_single_url):
                    img_list = self.__extract_img_socket(single_url_depth)
                    all_img_set.update(img_list)

                self.progress_bar_sender.progress.emit(i)
                if i == self.max_number_addresses:
                    break
        else:
            all_img_set = set(self.__extract_img_socket(addresses))

        return all_img_set

    def __get_all_urls_from_list(self, url_list: list):
        """
        List of lists mapping into single big list

        """
        urls = []
        for single_url in url_list:
            if isinstance(single_url, list):
                urls += self.__get_all_urls_from_list(single_url)
            else:
                urls += [single_url]

        return urls

    def __extract_img_socket(self, address) -> list:
        """
        Extract image names from certain `address`

        """
        try:
            html = self.__extract_html(address)

            # Create parser to find all images
            soup = BeautifulSoup(html, "html.parser")
            # Search images
            imgs_list = []
            for tag in soup.findAll("img"):
                src = tag.get('src')
                if src is not None:
                    imgs_list.append(src)

            return imgs_list
        except Exception as ex:
            print(f'Error: {ex}')
            return []

    def __extract_html(self, address):
        """
        Get html from certain address
        
        """

        # Separate path and link for main address
        f_ind, s_ind = self.__separe_path_and_address(address)
        if s_ind == -1:
            # There is only main address, for example: ssau.ru
            address = address[f_ind:]
            path = '/'
        else:
            # There is path and main address, for example: ssau.ru and ssau.ru/news
            address, path = (address[f_ind:s_ind], address[s_ind:])

        html = ""
        # Create and connect socket with server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((address, self.port))
            context = ssl.create_default_context()
            with context.wrap_socket(sock, server_hostname=address) as ssock:
                # Create message for server
                send_mess = f"GET {path} HTTP/1.0\r\n" \
                            f"Host: {address}\r\n" \
                            "Connection: close\r\n\r\n"

                # Send message
                ssock.send(send_mess.encode())

                # Grab all html text
                while True:
                    data = ssock.recv(self.REQUEST_SIZE_TO_READ)
                    if not data:
                        break
                    # Set ignore, if there is string with size lower than 4096
                    html += data.decode('utf-8', 'ignore')

        return html