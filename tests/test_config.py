import os
import unittest
import configparser
import simulate_register as srg
from cc_user import user
from pathlib import Path
from cc_config import config, token_tool


#create token before testing these.
#done!
class Config_testcases(unittest.TestCase):


    def test_delete_file(self):
        hidden_dir = str(Path.home())+'/.codeclinic/config.ini'
        if (os.path.exists(hidden_dir)):
            os.remove(hidden_dir)
        
        if (not os.path.exists(hidden_dir)):
            result = True
        self.assertTrue(result)


    def test_init_config(self):
        self.assertTrue(config.init_config())


    def test_read_config_true(self):
        self.assertTrue(config.read_config())


    def test_create_file(self):
        self.assertTrue(config.create_config())

    
    def test_register_user(self):
        token_name = user.create_token_name()
        token_result = token_tool.create_token(token_name)
        if (srg.del_account):
            result = srg.reg("1234", "abcd", "1234")
        self.assertTrue(result)

    
    def test_find_user(self):
        self.assertTrue(config.find_user("smciwa"))
    

    def test_read_user_config_true(self):
        self.assertTrue(config.read_user_config("smciwa"))

    
    def test_get_logged(self):
        self.assertTrue(config.get_logged())
    

    def test_delete_user(self):
        self.assertTrue(config.delete_user('smciwa'))

        