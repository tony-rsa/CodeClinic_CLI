import tempfile, os
from cc_user import user
from pathlib import Path
from datetime import datetime
from cc_booking import info, booking, volunteer
from icalendar import Calendar, Event, vCalAddress, vText
from cc_calendar import update_calendar, display_calendar

std_pointer = " \033[92m->\033[0m "
error_msg = " \u001b[33m[Error] \u001b[31m->\033[0m "

export_dir = str(Path.home()) + "/CodeClinic Exports/"

def add_attendee(email, role):
    """
        This function gets and returns attendee information
        :parm email: the users email
        :param role: the of the attendee
        :return attendee: the attendees info
    """
    attendee = vCalAddress('MAILTO:'+email)
    attendee.params['ROLE'] = vText(role)
    return attendee


def get_data():
    """
        This function retrives the users data.
        :returns data_dict:
    """
    update_calendar.update_calendars()
    campus = info.get_campus()
    data_dict = display_calendar.get_jhb_data()
    if campus == "cpt":
        print("cape town")
        data_dict = display_calendar.get_cpt_data()
    return data_dict


def export_to_ical():
    """
        This function exports the user bookings to ical format
        :return True: True if successful, false if not.
    """
    print(std_pointer+"Exporting your bookings..\n")
    email = info.get_email()
    data_dict = get_data()
    calendar = Calendar()
    calendar.add("title", "my code clinic bookings")
    count = 0
    for i in range(0, len(data_dict)):
        each = data_dict[list(data_dict.keys())[i]]
        event = None
        if each['volunteer'] == email or each['patient'] == email:
            count += 1
            event = Event()
            event_dt = list(data_dict.keys())[i]
            start_time = datetime.strptime(
                event_dt[:event_dt.find("+"):],'%Y-%m-%dT%H:%M:%S')
            event.add("uid", each["id"])
            event.add("summary", each["topic"])
            event.add("dtstart", start_time)
            event.add("attendee", add_attendee(
                str(each["volunteer"]), "volunteer"))
            event.add("attendee", add_attendee(
                str(each["patient"]), "patient"))
        if event != None:
            calendar.add_component(event)
            
    if count > 0:
        if not os.path.exists(export_dir):
            os.mkdir(export_dir)
        export_name = email[0:email.find("@"):] + "_bookings.ical"
        f = open(os.path.join(export_dir, export_name), 'wb')
        f.write(calendar.to_ical())
        f.close()
        print(std_pointer+f"Your bookings have \
successfully been exported to '{export_dir}'")
        return True
    print(error_msg+"You have no bookings to export, please book something.")
    return False
