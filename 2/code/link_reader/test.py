from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup
import socket
import ssl


def main():
    # 'https://ssau.ru/'
    # 'sixty-north.com', 443
    (port, adress) = (443, "ssau.ru")
    path = "/"

    html = ""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((adress, port))
        context = ssl.create_default_context()
        with context.wrap_socket(sock, server_hostname=adress) as ssock:

            send_mess = f"GET {path} HTTP/1.0\r\n" \
                        f"Host: {adress}\r\n" \
                        "Connection: close\r\n\r\n"

            ssock.send(send_mess.encode())

            while True:

                data = ssock.recv(4096)

                if not data:
                    break

                print(data.decode('utf-8', 'ignore'))
                html += data.decode('utf-8', 'ignore')

    soup = BeautifulSoup(html, "html.parser")

    print('len: ', len(soup.findAll("img")))

    img_tags = []
    # Search images
    for tag in soup.findAll("img"):
        img_tags.append(tag)

    urls = set()

    domain_name = urlparse(adress).netloc

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None or is_valid(href):
            # href empty tag
            continue
        # remove URL GET parameters, URL fragments, etc.
        href = urljoin(adress, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if href in urls:
            continue

        if domain_name not in href:
            # external link
            if href not in urls:
                print(f"[!] External link: {href}")
                urls.add(href)
            continue
        print(f"[*] Internal link: {href}")
        urls.add(href)

    print(urls.pop())


def main_old():
    adress = 'ssau.ru' #'https://ssau.ru/'
    #adress = 'sixty-north.com'
    port = 80 #443

    path = "/"

    html = ""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((adress, port))
        #socket.getaddrinfo('localhost', 25)
        """
        send_mess = f"GET {path}?request HTTP/1.0\r\n" \
                    f"Host: {adress}\r\n" \
                    "Content-Type: application/x-www-formurlencoded\r\n" \
                    f"Referer: {adress}\r\n\r\n"
        """
        send_mess = f"GET {path}?request HTTP/1.1\r\n" \
                    f"Host: {adress}\r\n" \
                    "Connection: close\r\n" \
                    f"Referer: {adress}\r\n" \
                    f"\r\n"

        s.sendall(send_mess.encode())

        while True:

            data = s.recv(4096)

            if not data:
                break

            print(data.decode())
            html += data.decode()

    soup = BeautifulSoup(html, "html.parser")

    print('len: ', len(soup.findAll("img")))

    img_tags = []
    # Search images
    for tag in soup.findAll("img"):
        img_tags.append(tag)

    print(img_tags[0].get('src'))


def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


if __name__ == "__main__":
    main()
