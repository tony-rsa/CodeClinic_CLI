import unittest
from cc_booking import booking

#done!
class BookingTestCases(unittest.TestCase):
    
    def test_is_volunteer_avail_False(self):
        """
        Checks if a particular date, is available
        for booking.
        """
        date_dict = {"2020-11-30T09:30:00+02:00": {"id": "5dfa5gt3ao08m6murk6eicj9ds", "topic": "Mastermind", 
                    "volunteer": "volunteer0000@example.com", "patient": "unittesta@gmail.com"}}
        
        start_time = "2020-11-30T09:30:00+02:00"
        email = "smciwa@student.wethinkcode.co.za"
        self.assertFalse(booking.is_volunteer_available(date_dict, start_time, email))
    

    def test_is_volunteer_avail_True(self):
        """
        Checks if a particular date, is available
        for booking.
        """
        date_dict = {"2020-11-30T09:30:00+02:00": {"id": "5dfa5gt3ao08m6murk6eicj9ds", "topic": "Mastermind", 
                    "volunteer": "volunteer0000@example.com", "patient": None}}
        
        start_time = "2020-11-30T09:30:00+02:00"
        email = "unittesta@gmail.com"
        self.assertTrue(booking.is_volunteer_available(date_dict, start_time, email))
    

    def test_get_volunteer_email(self):
        """
        Checks if volunteer's email is returned.
        """
        date_dict = {"2020-11-30T09:30:00+02:00": {"id": "5dfa5gt3ao08m6murk6eicj9ds", "topic": "Mastermind", 
                    "volunteer": "volunteer0000@example.com", "patient": None}}
        
        start_time = "2020-11-30T09:30:00+02:00"
        self.assertEqual(booking.get_volunteer_email(date_dict, start_time), "volunteer0000@example.com")

    
    def test_get_topic(self):
        """
        Checks if the topic is returned
        """
        date_dict = {"2020-11-30T09:30:00+02:00": {"id": "5dfa5gt3ao08m6murk6eicj9ds", "topic": "Mastermind", 
                    "volunteer": "volunteer0000@example.com", "patient": None}}
        
        start_time = "2020-11-30T09:30:00+02:00"
        self.assertEqual(booking.get_topic(date_dict, start_time), "Mastermind")
    

    def test_get_event_id(self):
        """
        Checks if the event id is returned
        """
        date_dict = {"2020-11-30T09:30:00+02:00": {"id": "5dfa5gt3ao08m6murk6eicj9ds", "topic": "Mastermind", 
                    "volunteer": "volunteer0000@example.com", "patient": None}}
        
        start_time = "2020-11-30T09:30:00+02:00"
        self.assertEqual(booking.get_event_id(date_dict, start_time), "5dfa5gt3ao08m6murk6eicj9ds")
