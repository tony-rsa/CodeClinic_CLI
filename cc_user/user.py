import datetime
from getpass import getpass
from cc_config import token_tool, config
from cc_user import encrypter, get_password

config.init_config()

std_pointer = " \033[92m->\033[0m "
error_span = "\n \033[93m[Error] \033[91m->\033[0m "

def create_token_name():
    """
        This function genarates a name for the user token.
        :return token_name: the created token_name.
    """
    token_name = ""
    token_name = token_name.join([c if c.isalpha() else ""\
                for c in encrypter.encrypt(str(datetime.datetime.now()))])
    return token_name


def create_user_creds(token_name, user_email, campus):
    """
        This function retrives the users creds and returns them in a list.
        :param token_name: the name of the token.
        :param user_email: the users email address.
        :param campus: the users campus cpt/jhb.
        :return list(): returns a list with user creds.
    """
    campus_dic = {"cpt" : 1, "jhb" : 2}
    user_name = str(user_email[:user_email.find("@"):])
    print("\n")
    campus_index = str(campus_dic[campus])
    password = str(encrypter.encrypt(get_password.get_password()))
    log_key = str(encrypter.encrypt("false"))
    return [user_email,user_name,campus_index,password,token_name, log_key]


def register(campus):
    """
        This funcrion register a new user by creating a new config and token.
        :param campus: the users campus cpt/jhb.
        :return True/False: True if successful, False if not.
    """
    token_name = create_token_name()
    token_result = token_tool.create_token(token_name)
    user_email = token_result[1]
    if token_result[0]:
        config.register_user(create_user_creds(token_name, user_email,campus))
        print("\n{} Using '{}' as your email address."\
            .format(std_pointer ,user_email))
        print("\t"+std_pointer+\
"User successfully register. Use \33[100m./cc login {}\33[0m and your \
password to login!\n".format(user_email[0:user_email.find("@")]))
        return True
    return False


def get_login_creds(user_name):
    """
        This function gets the users login creds using the users username.
        :param user_name: The users user name.
        :return (hashed, log_key, ask_password): user login creds in a tuple. 
    """
    if not config.find_user(user_name):
        print(error_span+\
            "User not found, please register or try again.\033")
        return False

    hashed = config.get_user_info(user_name,"user_hash")
    if not hashed:
        return False
    log_key = encrypter.encrypt("TRUE")
    ask_password = getpass(std_pointer+"Please enter password ")
    return (hashed, log_key, ask_password)


def login(user_name):
    """
        This function logs the user into the program using the users user_name.
        :param user_name: The users username.
        :return Ture/False: True if approved, False if not.
    """
    result = get_login_creds(user_name)
    if not result:
        return False

    hashed, log_key, password = result
    if encrypter.verify_encryption(password, hashed): 
        config.update_logged(str(datetime.datetime.now()),\
                                            log_key, user_name)
        print(std_pointer+"User approved for the next 20 mins.")
        print("\tUse \33[100m./cc calendar [number of days from 1 - 10]\33[0m\
 to view your campus calendar.")
        print("\tUse \33[100m./cc my_bookings\33[0m to view your bookings.")
        return True

    print(error_span+"User email or password incorrect.")
    return False


def get_datetime(login_time):
    """
        This function finds the users login window(20mins), 
        approved start and end time the user is alowed to be login at.
        :param login_time: The time the user logged in.
        :return login_start, login_end: the start and end time the user can be logged in for.
    """
    try:
        login_start = datetime.datetime.strptime(\
                    login_time.split('.')[0],'%Y-%m-%d %H:%M:%S')
    except ValueError:
        print(error_span+"Please Log in again!")
        return False

    login_end = login_start + datetime.timedelta(minutes=20)
    return login_start, login_end


def get_log_key():
    """
        This function get the users log key.
        :returns (login_time, log_key, user_name): users log key.
    """
    user_name  = config.get_logged()
    if not config.find_user(user_name):
        print(error_span+"Please login or register.")
        return False

    log_key  = config.get_user_info(user_name, "log_key")
    login_time = config.get_user_info(user_name, "login_time")
    if login_time == False or login_time == "0":
        print(error_span+"User is not logged in, please login!")
        print("\tUse \33[100m./cc login [username]\33[0m to login.")
        return False
    return (login_time, log_key, user_name)


def verify_user():
    """
        This function checks if the user is still logged in.
        :return True/False: True if the user is still logged in, False if not.
    """
    if not get_log_key():
        return False

    login_time , log_key, user_name = get_log_key()
    if not get_datetime(login_time):
        return False

    login_start, login_end = get_datetime(login_time)
    if login_start <= datetime.datetime.now() <= login_end and\
                     encrypter.verify_encryption("TRUE", log_key):
        print("\t\t\t\t\t\t\t\t\t\t\33[90mlogged in as '"\
            +user_name+"'.\33[0m\n")
        return True

    print(error_span+"User is not logged in.")
    print("\tUse \33[100m./cc login [username]\33[0m to login.")
    return False


def delete_user():
    """
        This function deletes a user.
        :return True/False: True if successful, False if not.
    """
    user_name  = config.get_logged()
    token_name = config.get_user_info(user_name, "user_token")
    if not token_name:
        return False

    config.delete_user(user_name)
    print(std_pointer+"User has been deleted successfully!")
    return token_tool.delete_token(token_name)


def verify_connection():
    """
        This function ping the user calendar to verify connection to the api.
        :return True/False: True if successful, False if not.
    """
    user_name  = config.get_logged()
    token_name = config.get_user_info(user_name, "user_token")
    if not token_name:
        return False
    print(std_pointer+"Trying to verfiy..")
    return token_tool.verify_token(token_name)


def logout():
    """
        This function logs the user out.
        :return True: if successful.
    """
    user_email  = config.get_logged()
    log_key  = encrypter.encrypt("False")
    config.update_logged("0", log_key, user_email)
    print(std_pointer+"User has been logged-out successfully.")
    print("\n\t\t\t\t\t\thave a nice day..")
    return True
