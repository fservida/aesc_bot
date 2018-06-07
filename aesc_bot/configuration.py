import logging

VERSION = 0.1

class Configuration:
    __instance = None

    def __init__(self):
        # Assert singleton
        if isinstance(Configuration.__instance, Configuration):
            raise AssertionError("This class is already instanciated")

        Configuration.__instance = self
        self.__help = {}
        self.__db = {"host": "localhost", "port": "3306"}
        self.__logger = None
        self.__version = VERSION

    @classmethod
    def get_instance(cls):
        return cls.__instance if isinstance(cls.__instance, Configuration) else Configuration()

    @property
    def help(self):
        return "\n".join(["/{} -> {}".format(command, helptext) for command, helptext in self.__help.items()])

    @help.setter
    def help(self, commands_file):
        with open(commands_file) as file:
            try:
                help_tmp = {commands[0].strip(): commands[1].strip() for commands in
                            [raw_commands.strip("\n").split("-") for raw_commands in file.readlines() if
                             raw_commands != "\n"]}
            except IndexError:
                raise ValueError("The command list file has an invalid format")
            self.__help = help_tmp

    @property
    def logger(self):
        return self.__logger

    @logger.setter
    def logger(self, logger):
        if not isinstance(logger, logging.Logger):
            raise ValueError("Invalid logger passed to configuration")
        else:
            self.__logger = logger

    @property
    def version(self):
        return "AESC Bot - Version: {}".format(self.__version)

if __name__ == '__main__':
    conf = Configuration.get_instance()
    print(conf.help)
    conf.help = "../command_list.txt"
    print(conf.help)
