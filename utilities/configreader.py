from configparser import ConfigParser


# config = ConfigParser()
#
# config.read("config.ini")
# print(config.get("locators","username"))

def ConfigRead(section, key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section, key)


print(ConfigRead("locators", "username"))
