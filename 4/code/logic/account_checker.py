from .config_controller import ConfigController
import smtplib


class AccountChecker:

    @staticmethod
    def password_check(user, psw) -> bool:
        host, port = ConfigController.get_current_params_for_sender()
        server = None
        try:
            server = smtplib.SMTP(host, port)
            server.starttls()
            server.login(user, psw)
            ret = True
        except:
            ret = False
        finally:
            if server is not None:
                server.quit()

        return ret

