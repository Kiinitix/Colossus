"""

This python file is a part of an open-source
project Colossus (https://github.com/Kiinitix/Colossus).

This file mainly focuses on creating configurations
file for easy setup of Colossus.

This must be the first file that you edit and run in
order to generate configurations.ini file for
improving security and easy setup.

Required fields -> sender_address, receiver_address, file_location, mailtrap_user, mailtrap_password

"""

import configparser

config_file = configparser.ConfigParser()
config_file.add_section("SMTPlogin")

# Add settings to section
# Here you need to modify the values of last parameter of set function
config_file.set("SMTPlogin", "sender_address", "----")
config_file.set("SMTPlogin", "receiver_address", "----")
config_file.set("SMTPlogin", "mailtrap_user", "----")
config_file.set("SMTPlogin", "mailtrap_password", "----")

# Saving config file as configurations.ini
with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")
