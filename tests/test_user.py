import unittest
import sys
import simulate_register
import simulate_login
from os import system
from io import StringIO
from unittest.mock import patch
from cc_user import user

class Test_User(unittest.TestCase):

    def test_verify_false(self):
        """
        Tries to verify user before registering.
        """
        error_span = " \033[93m[Error] \033[91m->\033[0m "
        sys.stdout = StringIO()
        system("./cc verify")
        user.verify_user()
        output = sys.stdout.getvalue()
        expected_output = "\n"+error_span+'Please login or register.\n'
        self.assertEqual(output, expected_output)
    

    def test_login_false(self):
        """
        Tries to login before registering.
        """
        system("./cc login smciwa")
        result = user.login("smciwa")
        self.assertFalse(result)


    def test_login_valid(self):
        result = simulate_login.login("1234")
        self.assertTrue(result)
    



