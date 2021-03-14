
def print_help():
    print(""" *** Note: These are the available commands in Code Clinic. ***

\t\33[6m Code Clinic Commands\33[0m

    \33[93m help                displays the description of each command.\33[0m
    register            registers a new user.
    login               logs the user into the system.
    verify              verifies whether the connection to Google calender was successful.
    calendar            displays the calender based on the user's campus.
    volunteer           volunteer for a time slot.
    book                book an available time slot.
    my_bookings         provides details of all the calendar events the user is involved in.
    export_bookings     exports the users booking to ical format.
    cancel_booking      enables the patient to remove themself from a booking.
    cancel_volunteer    enables the volunteer to remove the event from the calendar.
    delete_user         deletes the user's information and account.
    logout              logs the user out of the system.

 To get information about how to use a specific command:

     \33[100m./cc help [command]\33[0m

 Use the instruction provided above where [command], is one of the CODE CLINICS commands.
 *Note: do not include the square brackets.

 \tEXAMPLE: \33[100m./cc help login\33[0m""")


def export_bookings_help():
    print("""\n To export your bookings Use:
\t\33[100m./cc export_bookings\33[0m\n
 Your bookings will be exported to a file in '.ical' format.\n""")


def print_register_help():
    print(""" Use:
\t\33[100m./cc register [cpt/jhb]\33[0m\n
 You will be required to create a password.
 \n\tcpt - Cape town Campus.\n\tjhb - Johannesburg Campus.\n
 *** Note: Your password must have atleast 4 characters. ***""")
   

def print_login_help():
    print(""" To login, use:
\t\33[100m./cc login [username]\33[0m\n
 You will be asked to enter your password.\n
 *Note:
  - For [username], enter wtc_ username.
  - Use \33[100m./cc register [cpt/jhb]\33[0m if you do not have an account.\n""")


def print_verify_help():
    print(""" To verify connection to Google Calendar, login and use:\n
\t\33[100m./cc verify\33[0m\n
 *Note: A message will be displayed to confirm connection.""")


def print_calendar_help():
    print(""" To see the code clinic calendar, use:\n
\t\33[100m./cc calendar [number of days]\33[0m\n
 To view calendar:
  - [number of days] is optional.
  - For [number of days], enter a number between 1 and 10 inclusive.
  - If no number is specified it will default to 7.\n
 *Note:  The calendar will be displayed in a form of a table.""")


def print_delete_user_help():
    print(""" To delete your account, use:\n
\t\33[100m./cc delete_user\33[0m\n
 *Note: Your information will be erased from the system, and you will be 
        required to create a new account before using Code Clinics again.""")


def print_logout_help():
    print(""" To logout of the system, use:\n
\t\33[100m./cc logout\33[0m\n
 *Note: A message will be displayed to confirm you have logged out.\n""")


def print_volunteer_help():
    print(""" Use:
\t\33[100m./cc volunteer [date] [time] "topic"\33[0m\n
 To use volunteer:
  - For [date], enter date in format yyyy-mm-dd      eg. 2020-11-30
  - For [time], enter time in 24 hour format HH:MM   eg. 10:30
  - For "topic", enter topic of event with "".       eg. "Toy Robot"\n
 *** Note: Confirmation of event creation will be displayed. ***""")


def print_booking_help():
    print(""" Use:
\t\33[100m./cc book [date] [time]\33[0m\n
 To use book:
  - For [date], enter date in format yyyy-mm-dd      eg. 2020-11-30
  - For [time], enter time in 24 hour format HH:MM   eg. 10:30\n
 *** Note: Confirmation of booking will be displayed. ***""")


def print_my_bookings_help():
    print(""" Use:
\t\33[100m./cc my_bookings\33[0m\n
 To use my_bookings:\n
 *** Note: A list of your bookings with details will be displayed. ***""")


def print_cancel_booking_help():
    print(""" Use:
\t\33[100m./cc cancel_booking [event id]\33[0m\n
 To use cancel_booking:
  - For [event id], enter event id\n
 *** Note: please use my_bookings to obtain event id. ***""")


def print_cancel_volunteer_help():
    print(""" Use:
\t\33[100m./cc cancel_volunteer [event id]\33[0m\n
 To use cancel_volunteer:
  - For [event id], enter event id\n
 *** Note: please use my_bookings to obtain event id. ***""")


def get_help(args):
    """
    TODO: Receive one or two args
    """    
    help_options = {
        "help" : print_help, "register" : print_register_help,
        'login': print_login_help, 'verify': print_verify_help,
        'logout': print_logout_help, 'book': print_booking_help,
        'delete_user': print_delete_user_help, 
        'cancel_volunteer': print_cancel_volunteer_help,
        'volunteer': print_volunteer_help, 'calendar': print_calendar_help,
        'my_bookings': print_my_bookings_help,
        'cancel_booking': print_cancel_booking_help, "./cc" : print_help,
        'export_bookings' : export_bookings_help}

    try:
        args = args[len(args) - 1].lower()
        help_options[args]()
    except:
        print(f"'{args}' is not a Valid Code Clinic command.\n")
        return False
    return True
        