import getpass

std_pointer = "\033[92m->\033[0m "
error_msg = "\u001b[33m[Error] \033[92m->\033[0m "

def get_password():
    """
        This function asks the user for a password.
        :returns pwrd1/False: False if faild, pwrd1 if passed.
    """
    while True:
        pwrd1 = getpass.getpass("\n "+std_pointer+"Please create password ")
        pwrd2 = getpass.getpass("\t"+std_pointer+"Please confirm password ")
        if pwrd1 == pwrd2 and len(pwrd1) > 0:
            return pwrd1
        print(error_msg+"Passwords are invalid, try again!")
    return False