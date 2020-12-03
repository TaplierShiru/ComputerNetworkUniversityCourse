import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


class EmailSenderController:

    def __init__(self, login: str, password: str, host: str, port: int):

        self.__login = login
        self.__password = password

        self.__host = host
        self.__port = port

        self.error = None

    def send_message(self, header_str: str, text: str, send_to: list, attachment_path=None):

        server = self.__init_server()

        if attachment_path is not None:

            if isinstance(attachment_path, list):
                attachment_path = attachment_path[0]

            header = ('Content-Disposition', 'attachment')
        else:
            header = None

        # create the message
        msg = MIMEMultipart()
        msg["From"] = self.__login
        msg["Subject"] = header_str
        msg["Date"] = formatdate(localtime=True)
        msg.attach(MIMEText(text))
        msg["To"] = ', '.join(send_to)

        if header is not None:
            attachment = MIMEBase('application', "octet-stream")

            with open(attachment_path, "rb") as fh:
                data = fh.read()

            attachment.set_payload(data)
            encoders.encode_base64(attachment)
            attachment.add_header(*header, filename=attachment_path.split('/')[-1])
            msg.attach(attachment)

        server.sendmail(self.__login, send_to, msg.as_string())
        server.quit()
        self.error = None

    def __init_server(self) -> smtplib.SMTP:
        try:
            server = smtplib.SMTP(self.__host, port=self.__port)
        except Exception as exc:
            self.error = "Wrong host or port values"
            raise exc
        server.starttls()
        # Login Credentials for sending the mail
        server.login(self.__login, self.__password)
        return server
