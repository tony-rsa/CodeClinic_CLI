
import unittest
from tests import test_token_tool
from tests import test_config
from tests import test_user
from tests import test_booking
from tests import test_calendar
from tests import test_help


def Suite():
    suite = unittest.TestSuite()

    #---------- Token test ----------#
    TEST1 = test_token_tool.TokenTestCases("test_create_token")
    TEST2 = test_token_tool.TokenTestCases("test_load_token")
    TEST3 = test_token_tool.TokenTestCases("test_load_app_token")
    TEST4 = test_token_tool.TokenTestCases("test_get_email")
    TEST5 = test_token_tool.TokenTestCases("test_verify_token")
   

    #---------- Config test ----------#
    TEST6 = test_config.Config_testcases("test_delete_file")
    TEST7 = test_config.Config_testcases("test_init_config")
    TEST8 = test_config.Config_testcases("test_read_config_true")
    TEST9 = test_config.Config_testcases("test_create_file")
    TEST10 = test_user.Test_User("test_verify_false")
    TEST11 = test_user.Test_User("test_login_false")
    TEST12 = test_config.Config_testcases("test_register_user")
    TEST13 = test_config.Config_testcases("test_read_user_config_true")
    TEST14 = test_config.Config_testcases("test_find_user")
    TEST15 = test_config.Config_testcases("test_get_logged")
    TEST16 = test_user.Test_User("test_login_valid")

    #---------- Booking test ----------#

    TEST17 = test_booking.BookingTestCases("test_is_volunteer_avail_False")
    TEST18 = test_booking.BookingTestCases("test_is_volunteer_avail_True")
    TEST19 = test_booking.BookingTestCases("test_get_volunteer_email")
    TEST20 = test_booking.BookingTestCases("test_get_topic")
    TEST21 = test_booking.BookingTestCases("test_get_event_id")

    #---------- Calendar test ----------#

    TEST22 = test_calendar.Calendar_test("test_get_JHB_data")
    TEST23 = test_calendar.Calendar_test("test_get_CPT_data")
    TEST24 = test_calendar.Calendar_test("test_create_slots")
    TEST25 = test_calendar.Calendar_test("test_create_cal_files")

    #---------- help test ----------#

    TEST26 = test_help.Help_test("test_print_help_uppercase")
    TEST27 = test_help.Help_test("test_print_help_lowercase")
    TEST28 = test_help.Help_test("test_print_help_Mixedcase")
    TEST29 = test_help.Help_test("test_print_register_help_uppercase")
    TEST30 = test_help.Help_test("test_print_register_help_mixedcase")
    TEST31 = test_help.Help_test("test_print_register_help_lowercase")
    TEST32 = test_help.Help_test("test_print_login_help_uppercase")
    TEST33 = test_help.Help_test("test_print_login_help_lowercase")
    TEST34 = test_help.Help_test("test_print_login_help_mixedcase")
    TEST35 = test_help.Help_test("test_print_verify_help_uppercase")
    TEST36 = test_help.Help_test("test_print_verify_help_lowercase")
    TEST37 = test_help.Help_test("test_print_verify_help_mixedcase")
    TEST38 = test_help.Help_test("test_print_calendar_help_uppercase")
    TEST39 = test_help.Help_test("test_print_calendar_help_lowercase")
    TEST40 = test_help.Help_test("test_print_calendar_help_mixedcase")
    TEST41 = test_help.Help_test("test_print_delete_user_help_uppercase")
    TEST42 = test_help.Help_test("test_print_delete_user_help_lowercase")
    TEST43 = test_help.Help_test("test_print_delete_user_help_mixedcase")
    TEST44 = test_help.Help_test("test_print_logout_help_uppercase")
    TEST45 = test_help.Help_test("test_print_logout_help_lowercase")
    TEST46 = test_help.Help_test("test_print_logout_help_mixedrcase")
    TEST47 = test_help.Help_test("test_print_volunteer_help_uppercase")
    TEST48 = test_help.Help_test("test_print_volunteer_help_lowercase")
    TEST49 = test_help.Help_test("test_print_volunteer_help_mixedcase")
    TEST50 = test_help.Help_test("test_print_booking_help_uppercase")
    TEST51 = test_help.Help_test("test_print_booking_help_lowercase")
    TEST52 = test_help.Help_test("test_print_booking_help_mixedcase")
    TEST53 = test_help.Help_test("test_my_bookings_help_uppercase")
    TEST54 = test_help.Help_test("test_my_bookings_help_lowercase")
    TEST55 = test_help.Help_test("test_my_bookings_help_mixedcase")
    TEST56 = test_help.Help_test("test_print_cancel_booking_help_uppercase")
    TEST57 = test_help.Help_test("test_print_cancel_booking_help_lowercase")
    TEST58 = test_help.Help_test("test_print_cancel_booking_help_mixedcase")
    TEST59 = test_help.Help_test("test_print_cancel_vol_help_uppercase")
    TEST60 = test_help.Help_test("test_print_cancel_vol_help_lowercase")
    TEST61 = test_help.Help_test("test_print_cancel_vol_help_mixedcase")

    #should be last
    TEST62 = test_config.Config_testcases("test_delete_user")


    suite.addTest(TEST1)
    suite.addTest(TEST2)
    suite.addTest(TEST3)
    suite.addTest(TEST4)
    suite.addTest(TEST5)
    suite.addTest(TEST6)
    suite.addTest(TEST7)
    suite.addTest(TEST8)
    suite.addTest(TEST9)
    suite.addTest(TEST10)
    suite.addTest(TEST11)
    suite.addTest(TEST12)
    suite.addTest(TEST13)
    suite.addTest(TEST14)
    suite.addTest(TEST15)
    suite.addTest(TEST16)
    suite.addTest(TEST17)
    suite.addTest(TEST18)
    suite.addTest(TEST19)
    suite.addTest(TEST20)
    suite.addTest(TEST21)
    suite.addTest(TEST22)
    suite.addTest(TEST23)
    suite.addTest(TEST24)
    suite.addTest(TEST25)
    suite.addTest(TEST26)
    suite.addTest(TEST27)
    suite.addTest(TEST28)
    suite.addTest(TEST29)
    suite.addTest(TEST30)
    suite.addTest(TEST31)
    suite.addTest(TEST32)
    suite.addTest(TEST33)
    suite.addTest(TEST34)
    suite.addTest(TEST35)
    suite.addTest(TEST36)
    suite.addTest(TEST37)
    suite.addTest(TEST38)
    suite.addTest(TEST39)
    suite.addTest(TEST40)
    suite.addTest(TEST41)
    suite.addTest(TEST42)
    suite.addTest(TEST43)
    suite.addTest(TEST44)
    suite.addTest(TEST45)
    suite.addTest(TEST46)
    suite.addTest(TEST47)
    suite.addTest(TEST48)
    suite.addTest(TEST49)
    suite.addTest(TEST50)
    suite.addTest(TEST51)
    suite.addTest(TEST52)
    suite.addTest(TEST53)
    suite.addTest(TEST54)
    suite.addTest(TEST55)
    suite.addTest(TEST56)
    suite.addTest(TEST57)
    suite.addTest(TEST58)
    suite.addTest(TEST59)
    suite.addTest(TEST60)
    suite.addTest(TEST61)
    suite.addTest(TEST62)

    return (suite)

if __name__ == "__main__":
    
    runner = unittest.TextTestRunner()
    runner.run(Suite())