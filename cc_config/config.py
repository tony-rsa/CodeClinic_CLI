import os
import sys
import datetime
import configparser
from pathlib import Path

config = {}
user_config = {}
hidden_dir = str(Path.home())+'/.codeclinic'
error_span = "\033[93m[Error]\033[0m \033[91m->\033[0m"

def create_config():
    """
        This function creates the main config file in a hidden dir '~/.codeclinic/'
        :return True: If successful.
    """
    config = configparser.ConfigParser()
    config["LOGGED"] = {}
    config["LOGGED"] = {"user": "None"}
    with open(hidden_dir+'/config.ini', "w") as configfile:
            config.write(configfile)
    return True


def init_config():
    """
        Function makes creates hidden dir. and sub dir.
        :returns True: if successful.
    """
    if not os.path.exists(hidden_dir):
        os.mkdir(hidden_dir)
    if not os.path.exists(hidden_dir+"/token"):
        os.mkdir(hidden_dir+"/token")
    if not os.path.exists(hidden_dir+"/users"):
        os.mkdir(hidden_dir+"/users")
    if not os.path.exists(hidden_dir+"/config.ini"):
        create_config()
    return True


def write_config(config, config_dir, func):
    """
        This function creates a config in with the given dir and file name
        :param config: config phraser dict
        :param config-dir: The directory of the config file
        :param func: the open function to use, "w" or "a"
        :return True: If successful.
    """
    with open(hidden_dir+config_dir+'.ini', func) as configfile:
            config.write(configfile)
    return True


def register_user(config_dict):
    """
        Function updates the .ini file in hidden dir
        :param config_dict: a list [user_email, user_name, campus_index, password, token_name, log_key]
        :returns True:
    """
    config = configparser.ConfigParser()
    config["USER"] = {}
    config["USER"] = {'user_email': str(config_dict[0]),
        'user_name': config_dict[1],
        'user_hash': config_dict[3],
        'user_token': config_dict[4],
        'log_key' : config_dict[5],
        'login_time': str(0),
        'campus_index' : config_dict[2]}
    config_name = "/users/config"+config_dict[1]
    write_config(config, config_name, "w")
    return True


def find_user(user_name):
    """
    This function checks if a user already exists
    :return True/False: True if it does.
    """
    return os.path.exists(hidden_dir+"/users/config"+user_name+".ini")


def delete_user(user_name):
    """
        This function deletes a users config file
        :return True: if deleted
    """
    os.remove(hidden_dir+"/users/config"+user_name+".ini")
    return True


def read_user_config(user_name):
    """
        This funcion reads and store the users config in a global.
        :param user_name: the users username.
        :return True/False:True if completed, False if not.
    """
    global user_config

    user_config = configparser.ConfigParser()
    try:
        user_config.read(hidden_dir+"/users/config"+user_name+".ini")
    except configparser.ParsingError:
        print(error_span+"User not found, please register!")
        return False
    return True


def update_logged(login_time, log_key, user_name):
    """
        This function is used after a user has logged in, it update the users login creds and key
        :param login_time: the time the user logged in
        :param log_key: encrypted log key
        :param user_name: the users username
        :return True: True if successful.
    """
    global user_config, config

    if read_config() and read_user_config(user_name):
        config["LOGGED"]["user"] = str(user_name)
        user_config["USER"]['log_key'] = log_key
        user_config["USER"]['login_time'] = login_time
        write_config(user_config, "/users/config"+user_name, "w")
        write_config(config, "/config", "w")
    return True


def read_config():
    """
        This function reads the config files in the hidden dir to a global
        :return Ture: if successful.
    """
    global config

    config = configparser.ConfigParser()
    try:
        config.read(hidden_dir+"/config.ini")
    except:
        print(error_span+"Config not found. Please Login.")
        create_config()
        return False
    return True


def get_logged():
    """
        This function get the username of the logged in user
        :return username: The users username or False if user not found.
    """
    global config

    read_config()
    try:
        return config["LOGGED"]["user"]
    except:
        create_config()
        get_logged()
    return False


def get_user_info(user_name, option):
    """
        This function returns user info or creds that where asked for.
        :param user_name: the users username.
        :param option: The info that needs to be returned.
        :return : promted user info or False if error occoured.
    """
    global user_config

    read_user_config(user_name)
    if option == "user_token":
        if not os.path.exists(hidden_dir+"/token/"+\
                            user_config.get("USER", option)+".pickle"):
            print(error_span+"Token not found, please register.")
            return False
    try:
        return user_config.get("USER", option)
    except:
        pass

    print(error_span+":( User info compromised please register.")
    return False
    