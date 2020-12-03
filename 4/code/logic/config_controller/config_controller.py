import json


class ConfigController:

    __CURRENT_CONFIG = 'logic/config_controller/config.json'
    __DEFAULT_CONFIG = 'logic/config_controller/config_default.json'

    __RECEIVER = "receive"
    __SENDER = "send"
    __HOST = 'host'
    __PORT = 'port'

    @staticmethod
    def get_current_params_for_receiver():
        """

        Return host and port for receiver

        """
        with open(ConfigController.__CURRENT_CONFIG, 'r') as fp:
            data = json.load(fp)

        host = data[ConfigController.__HOST]
        port = data[ConfigController.__RECEIVER][ConfigController.__PORT]

        return host, port

    @staticmethod
    def get_current_params_for_sender():
        """

        Return host and port for sender

        """
        with open(ConfigController.__CURRENT_CONFIG, 'r') as fp:
            data = json.load(fp)

        host = data[ConfigController.__HOST]
        port = data[ConfigController.__SENDER][ConfigController.__PORT]

        return host, port

    def __init__(self):
        pass

    def change_host(self, host: str):
        if not isinstance(host, str):
            raise TypeError("Wrong type")

        data = self.__read_json()
        data[self.__HOST] = host
        self.__save_json(data)

    def change_receiver(self, port: int):

        if not isinstance(port, int):
            raise TypeError("Wrong type")

        data = self.__read_json()
        data[self.__RECEIVER][self.__PORT] = port

        self.__save_json(data)

    def change_sender(self,port: int):
        if not isinstance(port, int):
            raise TypeError("Wrong type")

        data = self.__read_json()
        data[self.__SENDER][self.__PORT] = port

        self.__save_json(data)

    def reset_params(self):
        data_default = self.__read_json(self.__DEFAULT_CONFIG)
        self.__save_json(data_default)

    def __read_json(self, config=None) -> dict:
        if config is None:
            config = self.__CURRENT_CONFIG

        with open(config, 'r') as fp:
            data = json.load(fp)

        return data

    def __save_json(self, data: dict):
        with open(self.__CURRENT_CONFIG, 'w') as fp:
            json.dump(data, fp)

