import unittest
import os
from pathlib import Path
from cc_booking import export_bookings

class TestFunctions(unittest.TestCase):

    def test_add_attendee(self):
        email = "@.mail"
        role = "volunteer"
        result = export_bookings.add_attendee(email, role)
        self.assertEqual(str(result), "MAILTO:@.mail")

    def test_get_data(self):
        export_bookings.update_calendar.update_calendars = lambda : print("", end="")
        export_bookings.display_calendar.get_jhb_data = lambda : {"jhb bookings"}
        export_bookings.display_calendar.get_cpt_data = lambda : {"cpt bookings"}
        export_bookings.info.get_campus = lambda :"jhb"
        data_dict = export_bookings.get_data()
        self.assertEqual(data_dict, {'jhb bookings'})
        export_bookings.info.get_campus = lambda :"cpt"
        data_dict = export_bookings.get_data()
        self.assertEqual(data_dict, {'cpt bookings'})

    def test_to_ical(self):
        bookings = {"2020-12-14T12:00:00+02:00": {"id": "0prdm15p37h6r8ebb34pb9ks10",\
             "topic": "Lists", "volunteer": "volunteer0000@example.com",\
            "patient": "testmail@.mail"}, "2020-12-14T12:30:00+02:00":\
             {"id": "3jrk6e7sim8vrddq10sgqnp85t", "topic": "Topic", \
            "volunteer": "testmail@.mail", "patient": "p@c.com"}}

        export_bookings.get_data = lambda : bookings
        export_bookings.info.get_email = lambda : "testmail@.mail"
        export_bookings.export_to_ical()
        export_dir = str(Path.home()) + "/CodeClinic Exports/"
        self.assertTrue(os.path.exists(export_dir+"testmail_bookings.ical"))
        if os.path.exists(export_dir+"testmail_bookings.ical"):
            os.remove(export_dir+"testmail_bookings.ical")