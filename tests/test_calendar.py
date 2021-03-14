import unittest
from cc_calendar import display_calendar as display
from cc_calendar import update_calendar as update

#done!
class Calendar_test(unittest.TestCase):

    def test_get_JHB_data(self):
        self.assertIsInstance(display.get_jhb_data(), dict)
    

    def test_get_CPT_data(self):
        self.assertIsInstance(display.get_cpt_data(), dict)


    def test_create_slots(self):
        self.assertIsInstance(display.create_slot_dict(), dict)
    

    def test_create_cal_files(self):
        self.assertTrue(update.create_calendar_files())