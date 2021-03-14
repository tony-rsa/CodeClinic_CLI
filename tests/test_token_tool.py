import unittest
from io import StringIO
import sys
from cc_config import token_tool

#done!
class TokenTestCases(unittest.TestCase):

    def test_create_token(self):
        token_name = 'app_token.pickle'
        token_tool.create_token(token_name)
        sys.stdout = StringIO()
        result = token_tool.verify_token(token_name)
        output = sys.stdout.getvalue()
        self.assertTrue(result)
    

    def test_load_token(self):
        self.assertNotEqual(token_tool.load_token("app_token.pickle"), None)
    

    def test_load_app_token(self):
        self.assertNotEqual(token_tool.load_app_token(), None)
    

    def test_get_email(self):
        self.assertIn("@", token_tool.get_email("app_token.pickle"))
    

    def test_verify_token(self):
        token_name = 'app_token.pickle'
        sys.stdout = StringIO()
        result = token_tool.verify_token(token_name)
        output = sys.stdout.getvalue()
        self.assertTrue(result)
        
    
    def test_delete_token(self):
        token_name = 'app_token.pickle'
        result = token_tool.delete_token(token_name)
        self.assertTrue(result)
    


