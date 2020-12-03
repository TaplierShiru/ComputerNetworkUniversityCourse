from .content_wrapper import Content

import email
import os
import poplib


class EmailReceiverController:

    def __init__(self, login: str, password: str, host: str, port: int):

        self.__login = login
        self.__password = password

        self.__host = host
        self.__port = port

        self.__last_update_content = None
        self.error = None

    def take_content_from_new_mess(self, save_files_to: str) -> list:
        """

        Return list of object: Content

        """
        try:
            box = poplib.POP3_SSL(self.__host, self.__port)
        except Exception as exc:
            self.error = "Wrong host or port values"
            raise exc

        box.user(self.__login)
        box.pass_(self.__password)

        response, lst, octets = box.list()
        print("DEBUG: Total %s messages: %s" % (self.__login, len(lst)))

        final_content_list = []
        messages = [box.retr(i) for i in range(1, len(box.list()[1]) + 1)]

        for i in range(len(messages)):
            content_box = Content()
            final_content_list.append(content_box)

            single_mess = messages[i][1]

            str_message = email.message_from_bytes(b'\n'.join(single_mess))

            multipart_was_found = False
            # save attach and other things
            for part in str_message.walk():

                if not multipart_was_found and part.get_content_maintype() == 'multipart':
                    charset = part.get_charset()
                    # if can not get charset.
                    if charset is None:
                        # get message 'Content-Type' header value.
                        content_type = part.get('From', '')
                        if "<" in content_type:
                            # Message from: dadawd=adawdwa=<email@some.com>
                            # Grab email@some.com
                            content_type = content_type.split('<')[1].split('>')[0]

                        content_box.from_txt = content_type
                        content_box.header_txt = part.get('Subject', '')
                        content_box.date = part.get('Date')
                        multipart_was_found = True
                        continue

                if part.get_content_type() == 'text/plain':
                    # get text content.
                    content = part.get_payload(decode=True)
                    # get text charset.
                    charset = part.get_charset()
                    # if can not get charset.
                    if charset is None:
                        # get message 'Content-Type' header value.
                        content_type = part.get('Content-Type', '').lower()
                        # parse the charset value from 'Content-Type' header value.
                        pos = content_type.find('charset=')
                        if pos >= 0:
                            charset = content_type[pos + 8:].strip()
                            pos = charset.find(';')
                            if pos >= 0:
                                charset = charset[0:pos]
                    if charset:
                        content = content.decode(charset)
                    content_box.full_txt = content

                filename = part.get_filename()
                if not (filename): continue

                path_to_file = save_files_to + '/' + filename
                fp = open(path_to_file, 'wb')
                fp.write(part.get_payload(decode=1))
                fp.close()

                content_box.attach = path_to_file

        box.quit()
        self.error = None

        self.__last_update_content = final_content_list
        return final_content_list

    def get_last_update(self) -> Content:
        return self.__last_update_content

