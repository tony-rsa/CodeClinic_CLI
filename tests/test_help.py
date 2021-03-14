import unittest
import sys
from os import system
from io import StringIO
from cc_help import get_help as Help

class Help_test(unittest.TestCase):

    def test_print_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP")
        Help.print_help()
        output = sys.stdout.getvalue()
        self.assertTrue("Code Clinic Commands" in output)

    
    def test_print_register_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP REGISTER")
        Help.print_register_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc register [cpt/jhb]\33[0m\n
 You will be required to create a password.
 \n\tcpt - Cape town Campus.\n\tjhb - Johannesburg Campus.\n
 *** Note: Your password must have atleast 4 characters. ***
"""
        self.assertEqual(output, expected_output)

    
    def test_print_register_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help register")
        Help.print_register_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc register [cpt/jhb]\33[0m\n
 You will be required to create a password.
 \n\tcpt - Cape town Campus.\n\tjhb - Johannesburg Campus.\n
 *** Note: Your password must have atleast 4 characters. ***
"""
        self.assertEqual(output, expected_output)


    def test_print_register_help_mixedcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HeLp rEgIsTeR")
        Help.print_register_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc register [cpt/jhb]\33[0m\n
 You will be required to create a password.
 \n\tcpt - Cape town Campus.\n\tjhb - Johannesburg Campus.\n
 *** Note: Your password must have atleast 4 characters. ***
"""
        self.assertEqual(output, expected_output)


    def test_print_login_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP LOGIN")
        Help.print_login_help()
        output = sys.stdout.getvalue()
        expected_output = """ To login, use:
\t\33[100m./cc login [username]\33[0m\n
 You will be asked to enter your password.\n
 *Note:
  - For [username], enter wtc_ username.
  - Use \33[100m./cc register [cpt/jhb]\33[0m if you do not have an account.\n
"""
        self.assertEqual(output, expected_output)

    
    def test_print_login_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help login")
        Help.print_login_help()
        output = sys.stdout.getvalue()
        expected_output = """ To login, use:
\t\33[100m./cc login [username]\33[0m\n
 You will be asked to enter your password.\n
 *Note:
  - For [username], enter wtc_ username.
  - Use \33[100m./cc register [cpt/jhb]\33[0m if you do not have an account.\n
"""
        self.assertEqual(output, expected_output)


    def test_print_login_help_mixedcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HeLp lOgIn")
        Help.print_login_help()
        output = sys.stdout.getvalue()
        expected_output = """ To login, use:
\t\33[100m./cc login [username]\33[0m\n
 You will be asked to enter your password.\n
 *Note:
  - For [username], enter wtc_ username.
  - Use \33[100m./cc register [cpt/jhb]\33[0m if you do not have an account.\n
"""
        self.assertEqual(output, expected_output)


    def test_print_verify_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP VERIFY")
        Help.print_verify_help()
        output = sys.stdout.getvalue()
        expected_output = """ To verify connection to Google Calendar, login and use:\n
\t\33[100m./cc verify\33[0m\n
 *Note: A message will be displayed to confirm connection.
"""
        self.assertEqual(output, expected_output)


    def test_print_verify_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help verify")
        Help.print_verify_help()
        output = sys.stdout.getvalue()
        expected_output = """ To verify connection to Google Calendar, login and use:\n
\t\33[100m./cc verify\33[0m\n
 *Note: A message will be displayed to confirm connection.
"""
        self.assertEqual(output, expected_output)

    def test_print_verify_help_mixedcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HeLp vErIfY")
        Help.print_verify_help()
        output = sys.stdout.getvalue()
        expected_output = """ To verify connection to Google Calendar, login and use:\n
\t\33[100m./cc verify\33[0m\n
 *Note: A message will be displayed to confirm connection.
"""
        self.assertEqual(output, expected_output)


    def test_print_calendar_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP CALENDAR")
        Help.print_calendar_help()
        output = sys.stdout.getvalue()
        expected_output = """ To see the code clinic calendar, use:\n
\t\33[100m./cc calendar [number of days]\33[0m\n
 To view calendar:
  - [number of days] is optional.
  - For [number of days], enter a number between 1 and 10 inclusive.
  - If no number is specified it will default to 7.\n
 *Note:  The calendar will be displayed in a form of a table.
"""
        self.assertEqual(output, expected_output)


    def test_print_calendar_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help calendar")
        Help.print_calendar_help()
        output = sys.stdout.getvalue()
        expected_output = """ To see the code clinic calendar, use:\n
\t\33[100m./cc calendar [number of days]\33[0m\n
 To view calendar:
  - [number of days] is optional.
  - For [number of days], enter a number between 1 and 10 inclusive.
  - If no number is specified it will default to 7.\n
 *Note:  The calendar will be displayed in a form of a table.
"""
        self.assertEqual(output, expected_output)


    def test_print_calendar_help_mixedcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc hElP CaLeNdAr")
        Help.print_calendar_help()
        output = sys.stdout.getvalue()
        expected_output = """ To see the code clinic calendar, use:\n
\t\33[100m./cc calendar [number of days]\33[0m\n
 To view calendar:
  - [number of days] is optional.
  - For [number of days], enter a number between 1 and 10 inclusive.
  - If no number is specified it will default to 7.\n
 *Note:  The calendar will be displayed in a form of a table.
"""
        self.assertEqual(output, expected_output)


    def test_print_delete_user_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP DELETE_USER")
        Help.print_delete_user_help()
        output = sys.stdout.getvalue()
        expected_output = """ To delete your account, use:\n
\t\33[100m./cc delete_user\33[0m\n
 *Note: Your information will be erased from the system, and you will be 
        required to create a new account before using Code Clinics again.
"""
        self.assertEqual(output, expected_output)

    
    def test_print_delete_user_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help delete_user")
        Help.print_delete_user_help()
        output = sys.stdout.getvalue()
        expected_output = """ To delete your account, use:\n
\t\33[100m./cc delete_user\33[0m\n
 *Note: Your information will be erased from the system, and you will be 
        required to create a new account before using Code Clinics again.
"""
        self.assertEqual(output, expected_output)

    
    def test_print_delete_user_help_mixedcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP dElEtE_uSeR")
        Help.print_delete_user_help()
        output = sys.stdout.getvalue()
        expected_output = """ To delete your account, use:\n
\t\33[100m./cc delete_user\33[0m\n
 *Note: Your information will be erased from the system, and you will be 
        required to create a new account before using Code Clinics again.
"""
        self.assertEqual(output, expected_output)


    def test_print_logout_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP LOGOUT")
        Help.print_logout_help()
        output = sys.stdout.getvalue()
        expected_output = """ To logout of the system, use:\n
\t\33[100m./cc logout\33[0m\n
 *Note: A message will be displayed to confirm you have logged out.\n
"""
        self.assertEqual(output, expected_output)

    
    def test_print_logout_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help logout")
        Help.print_logout_help()
        output = sys.stdout.getvalue()
        expected_output = """ To logout of the system, use:\n
\t\33[100m./cc logout\33[0m\n
 *Note: A message will be displayed to confirm you have logged out.\n
"""
        self.assertEqual(output, expected_output)
    

    def test_print_logout_help_mixedrcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc hElP lOgOuT")
        Help.print_logout_help()
        output = sys.stdout.getvalue()
        expected_output = """ To logout of the system, use:\n
\t\33[100m./cc logout\33[0m\n
 *Note: A message will be displayed to confirm you have logged out.\n
"""
        self.assertEqual(output, expected_output)


    def test_print_volunteer_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP VOLUNTEER")
        Help.print_volunteer_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc volunteer [date] [time] "topic"\33[0m\n
 To use volunteer:
  - For [date], enter date in format yyyy-mm-dd      eg. 2020-11-30
  - For [time], enter time in 24 hour format HH:MM   eg. 10:30
  - For "topic", enter topic of event with "".       eg. "Toy Robot"\n
 *** Note: Confirmation of event creation will be displayed. ***
"""
        self.assertEqual(output, expected_output)

    def test_print_volunteer_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help volunteer")
        Help.print_volunteer_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc volunteer [date] [time] "topic"\33[0m\n
 To use volunteer:
  - For [date], enter date in format yyyy-mm-dd      eg. 2020-11-30
  - For [time], enter time in 24 hour format HH:MM   eg. 10:30
  - For "topic", enter topic of event with "".       eg. "Toy Robot"\n
 *** Note: Confirmation of event creation will be displayed. ***
"""
        self.assertEqual(output, expected_output)


    def test_print_volunteer_help_mixedcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HeLp VoLnNtEeR")
        Help.print_volunteer_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc volunteer [date] [time] "topic"\33[0m\n
 To use volunteer:
  - For [date], enter date in format yyyy-mm-dd      eg. 2020-11-30
  - For [time], enter time in 24 hour format HH:MM   eg. 10:30
  - For "topic", enter topic of event with "".       eg. "Toy Robot"\n
 *** Note: Confirmation of event creation will be displayed. ***
"""
        self.assertEqual(output, expected_output)


    def test_print_booking_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP BOOK")
        Help.print_booking_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc book [date] [time]\33[0m\n
 To use book:
  - For [date], enter date in format yyyy-mm-dd      eg. 2020-11-30
  - For [time], enter time in 24 hour format HH:MM   eg. 10:30\n
 *** Note: Confirmation of booking will be displayed. ***
"""
        self.assertEqual(output, expected_output)

    
    def test_print_booking_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help book")
        Help.print_booking_help()
        output = sys.stdout.getvalue()
        expected_output =  """ Use:
\t\33[100m./cc book [date] [time]\33[0m\n
 To use book:
  - For [date], enter date in format yyyy-mm-dd      eg. 2020-11-30
  - For [time], enter time in 24 hour format HH:MM   eg. 10:30\n
 *** Note: Confirmation of booking will be displayed. ***
"""
        self.assertEqual(output, expected_output)


    def test_print_booking_help_mixedcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HeLp bOoK")
        Help.print_booking_help()
        output = sys.stdout.getvalue()
        expected_output =  """ Use:
\t\33[100m./cc book [date] [time]\33[0m\n
 To use book:
  - For [date], enter date in format yyyy-mm-dd      eg. 2020-11-30
  - For [time], enter time in 24 hour format HH:MM   eg. 10:30\n
 *** Note: Confirmation of booking will be displayed. ***
"""
        self.assertEqual(output, expected_output)


    def test_my_bookings_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP MY_BOOKINGS")
        Help.print_my_bookings_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc my_bookings\33[0m\n
 To use my_bookings:\n
 *** Note: A list of your bookings with details will be displayed. ***
"""
        self.assertEqual(output, expected_output)


    def test_my_bookings_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help my_bookings")
        Help.print_my_bookings_help()
        output = sys.stdout.getvalue()
        expected_output =  """ Use:
\t\33[100m./cc my_bookings\33[0m\n
 To use my_bookings:\n
 *** Note: A list of your bookings with details will be displayed. ***
"""
        self.assertEqual(output, expected_output)


    def test_my_bookings_help_mixedcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HeLp mY_bOoKiNgS")
        Help.print_my_bookings_help()
        output = sys.stdout.getvalue()
        expected_output =  """ Use:
\t\33[100m./cc my_bookings\33[0m\n
 To use my_bookings:\n
 *** Note: A list of your bookings with details will be displayed. ***
"""
        self.assertEqual(output, expected_output)


    def test_print_cancel_booking_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP CANCEL_BOOKING")
        Help.print_cancel_booking_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc cancel_booking [event id]\33[0m\n
 To use cancel_booking:
  - For [event id], enter event id\n
 *** Note: please use my_bookings to obtain event id. ***
"""
        self.assertEqual(output, expected_output)
    
    def test_export_help(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc export_bookings")
        output = sys.stdout.getvalue()
        self.assertFalse("Exporting your bookings." in output)

    def test_print_cancel_booking_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help cancel_booking")
        Help.print_cancel_booking_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc cancel_booking [event id]\33[0m\n
 To use cancel_booking:
  - For [event id], enter event id\n
 *** Note: please use my_bookings to obtain event id. ***
"""
        self.assertEqual(output, expected_output)


    def test_print_cancel_booking_help_mixedcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HeLp CanCeL_bOoKiNg")
        Help.print_cancel_booking_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc cancel_booking [event id]\33[0m\n
 To use cancel_booking:
  - For [event id], enter event id\n
 *** Note: please use my_bookings to obtain event id. ***
"""
        self.assertEqual(output, expected_output)


    def test_print_cancel_vol_help_uppercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HELP VOLUNTEER")
        Help.print_cancel_volunteer_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc cancel_volunteer [event id]\33[0m\n
 To use cancel_volunteer:
  - For [event id], enter event id\n
 *** Note: please use my_bookings to obtain event id. ***
"""
        self.assertEqual(output, expected_output)


    def test_print_cancel_vol_help_lowercase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc help volunteer")
        Help.print_cancel_volunteer_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc cancel_volunteer [event id]\33[0m\n
 To use cancel_volunteer:
  - For [event id], enter event id\n
 *** Note: please use my_bookings to obtain event id. ***
"""
        self.assertEqual(output, expected_output)


    def test_print_cancel_vol_help_mixedcase(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        system("./cc HeLp CanCeL_vOlUnTeEr")
        Help.print_cancel_volunteer_help()
        output = sys.stdout.getvalue()
        expected_output = """ Use:
\t\33[100m./cc cancel_volunteer [event id]\33[0m\n
 To use cancel_volunteer:
  - For [event id], enter event id\n
 *** Note: please use my_bookings to obtain event id. ***
"""
        self.assertEqual(output, expected_output)