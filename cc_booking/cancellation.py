from cc_config import token_tool
from cc_booking import info, booking, volunteer
from cc_calendar import update_calendar, display_calendar

error_span = "\n \033[93m[Error] \033[91m->\033[0m "
std_pointer = " \033[92m->\033[0m "

def get_volunteer_email(data_dict, event_id):
    """
    Retrieves the volunteers email from dictionary.
    parameters: data_dict: the dictionary of events
                event_id: the id of event
    returns: the volunteers email
    """
    for i in data_dict:
        if data_dict[i]['id'] == event_id:
            return data_dict[i]['volunteer']


def can_patient_cancel(data_dict, event_id, email):
    """
    Checks the dictionary if user is the patient for specified event
    parameters: data_dict: dictionary of events
                event_id : event id from command line
                email : users email
    return: True if user is patient of event, false if not
    """
    for i in data_dict:
        if data_dict[i]['id'] == event_id and \
                            data_dict[i]['patient'] == email:
            return True
    return False


def can_volunteer_cancel(data_dict, event_id, email):
    """
    Checks the dictionary if the volunteer can cancel event
    parameters: data_dict: dictionary of events
                event_id : event id from command line
                email : users email
    return: True if user is volunteer and no patient assigned of event, False if not
    """
    for i in data_dict:
        if data_dict[i]['id'] == event_id and \
                        data_dict[i]['volunteer'] == email:
            if data_dict[i]['patient'] is None:
                return True
    return False


def remove_patient(service, calendar_id, event_id, volunteer_email):
    """
    Updates the events attendee list by removing patients email and sends notifications to attendees.
    parameters: service: google calendar api service
                calendar_id: the calendar id of the calendar to update
                event_id: the evnt id of the event to update
                volunteer_email: the volunteers email
    """
    event = service.events().get(calendarId=calendar_id,\
         eventId=event_id).execute()

    event['attendees'] = [{'email' : volunteer_email,
    'responseStatus' : 'accepted'}]

    updated_event = service.events().update(calendarId=calendar_id,\
         eventId=event['id'], body=event, sendUpdates='all').execute()


def cancel_event(service, calendar_id, event_id):
    """
    Deletes volunteers event
    parameters: service: google calendar api service
                calendar_id : the calendar id of calendar to update
                event_id : the id of event to delete
    """
    service.events().delete(calendarId=calendar_id, \
        eventId=event_id, sendUpdates='all').execute()


def cancel_booking():
    update_calendar.update_calendars()
    campus = info.get_campus()
    if campus == 'cpt':
        data = display_calendar.get_cpt_data()
    elif campus == 'jhb':
        data = display_calendar.get_jhb_data()
    email = info.get_email()
    event_id = info.get_event_id()
    if can_patient_cancel(data, event_id, email):
        service = token_tool.load_app_token()
        calendar_id = info.get_calendar_id()
        volunteer_email = get_volunteer_email(data, event_id)
        remove_patient(service, calendar_id, event_id, volunteer_email)
        print(std_pointer+
        'You have successfully been removed from booking with event id : {}'\
        .format(event_id))
    else:
        print(error_span+'You cannot cancel this booking.')


def cancel_volunteer():
    update_calendar.update_calendars()
    campus = info.get_campus()
    if campus == 'cpt':
        data = display_calendar.get_cpt_data()
    elif campus == 'jhb':
        data = display_calendar.get_jhb_data()
    event_id = info.get_event_id()
    email = info.get_email()
    if can_volunteer_cancel(data, event_id, email):
        service = token_tool.load_app_token()
        calendar_id = info.get_calendar_id()
        cancel_event(service, calendar_id, event_id)
        print(std_pointer+\
        'You have successfully canceled event with event id : {}'\
        .format(event_id))
    else:
        print(error_span+'You cannot cancel this booking.')