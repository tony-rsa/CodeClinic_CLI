#!/usr/bin/env python3

import sys
from cc_user import user
from cc_config import config, token_tool
from cc_help import get_help
from cc_booking import export_bookings
from cc_calendar import display_calendar
from cc_booking import volunteer, booking, view_bookings, cancellation

error_msg = " \u001b[33m[Error] \u001b[31m->\033[0m "

def check_valid_arg(arg):
    """
        This check to see if the given arg is valid.
        :param arg: input command line arguments.
        :returns true/false: ture if arg valid, false if not.
    """
    valid_arg = {'login' : 3, 'help' : 3,'register' : 3, 
                'verify': 2, 'delete_user' : 2, 'logout' : 2, 
                'calendar' : 2, 'volunteer' : 5, 'book' : 4,
                'my_bookings' : 2,'cancel_booking' : 3, 
                'cancel_volunteer' : 3, "export_bookings" : 2}

    valid_campus = ["cpt", "jhb"]

    if len(arg) > 1:
        if (arg[1] == 'calendar' and len(arg) == 3) or\
            (arg[1] in valid_arg.keys() and \
                        len(arg) == valid_arg[arg[1]]):
            if arg[1] == "register" \
                            and not arg[2] in valid_campus:
                return False
            return True
    return False


def get_argument():
    """
        This function get and returns args.
        :returns arg: command line arguments, or empty string.
    """
    arg = [x.lower() for x in sys.argv]
    if check_valid_arg(arg) or ("help" in arg and len(arg) == 2):
        return arg
    print(error_msg+"Invalid arguments.\n")
    print("\tPlease try \33[100m./cc help\33[0m\n")
    return False


def check_internet_con():
    """
        This functions check if its possible to connect to the api.
        :return True/False: True if possible, False if not.
    """
    if token_tool.load_app_token() == None:
        print(error_msg+
            "Can't connect to APi, \
Please make sure you are connected to the internet!")
        return False
    return True

    
def begin():
    """
        This function starts the program.
    """
    run_ = {"calendar" : display_calendar.print_calendar,
            "cancel_booking" : cancellation.cancel_booking,
            'book': booking.book,
            "my_bookings": view_bookings.view_bookings,
            'volunteer' : volunteer.volunteer,
            "verify" : user.verify_connection,
            "cancel_volunteer" : cancellation.cancel_volunteer,
            "export_bookings" : export_bookings.export_to_ical}
    
    arg = get_argument()

    if arg == False:
        return -1
    
    if "help" in arg:
        get_help.get_help(arg)
        return -1

    if not check_internet_con():
        return -1

    if "register" in arg:
        user.register(arg[len(arg)-1])
        return -1
        
    if "login" in arg:
        user.login(arg[len(arg)-1])
        return -1

    if not user.verify_user():
        return -1

    if 'logout' in arg:
        user.logout()
        return -1

    if "delete_user" in arg: 
        user.delete_user()
        return -1

    run_[arg[1]]()
    return 0


if __name__ == "__main__" :
    
    if begin() == 0:
        print("\n\t\t\t\t\t\t\t\t\t\tUse\
 \33[100m./cc logout\33[0m to logout.")


