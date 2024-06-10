''' from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key) '''

import configparser


class ReadConfigurations:
    @staticmethod
    def read_configuration(section, key):
        config = configparser.ConfigParser()
        config.read("C:\\Users\\N.JANDOUBI\\OneDrive - SEPTEO\\Bureau\\SeleniumPythonHybridFramework\\configurations"
                    "\\config.ini")

        if not config.has_section(section):
            raise configparser.NoSectionError(section)

        if not config.has_option(section, key):
            raise configparser.NoOptionError(key, section)

        return config.get(section, key)
