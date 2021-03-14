import random
from cc_booking import info
from cc_config import token_tool
from cc_calendar import update_calendar, display_calendar


error_span = "\n \033[93m[Error] \033[91m->\033[0m "

def is_volunteer_available(data_dict, start_time, email):
    """
    Checks the dictionary if time slot at starttime exists and if available for patient.
    parameters: data_dict: the dictionary of events
                start_time: the date and time of event
                email: the email of the user
    returns: available: True if slot is available
                        False if slot is unavailble
    """
    available = False
    if start_time in data_dict.keys():
        if data_dict[start_time]['patient'] is None:
            available = True
        if data_dict[start_time]['volunteer'] == email:
            available = False
    return available


def create_random_id():
    """
    creates a random id for the calendar api
    returns: random_id
    """
    alpha = 'abcdefghijklmnopqrstuvwxyz1234567890'
    random_id = ''
    random_id += ''.join(random.choice(alpha) for x in range(16))
    return random_id


def get_volunteer_email(data_dict, start_time):
    """
    Retrieves the volunteers email from dictionary.
    parameters: data_dict: the dictionary of events
                start_time: the start date and time of event
    returns: the volunteers email
    """
    if start_time in data_dict.keys():
        return data_dict[start_time]['volunteer']


def get_topic(data_dict, start_time):
    """
    Retrieves the topic from dictionary.
    parameters: data_dict: the dictionary of events
                start_time: the start date and time of event
    returns: the topic
    """
    if start_time in data_dict.keys():
        return data_dict[start_time]['topic']


def get_event_id(data_dict, start_time):
    """
    Retrieves the event id from dictionary.
    parameters: data_dict: the dictionary of events
                start_time: the start date and time of event
    returns: the event id
    """
    if start_time in data_dict.keys():
        return data_dict[start_time]['id']


def add_patient(service, calendar_id, event_id, volunteer_email, email, random_id):
    """
    Updates the events attendee list with patients email and sends notifications to attendees.
    parameters: service: google calendar api service
                calendar_id: the calendar id of the calendar to update
                event_id: the evnt id of the event to update
                volunteer_email: the volunteers email
                email: the users email
    """
    event = service.events().get(calendarId=calendar_id, \
            eventId=event_id).execute()

    event['attendees'] = [{'email' : volunteer_email,
    'responseStatus' : 'accepted'},
    {'email' : email,
    'responseStatus' : 'accepted'}]
    event['conferenceData'] = {
            'createRequest': {
                'requestID': random_id,
                'conferenceSolutionKey': {
                    'type': 'hangoutsMeet'
                }}}

    updated_event = service.events().update(calendarId=calendar_id, \
                    eventId=event['id'], body=event, sendUpdates='all',\
                    conferenceDataVersion=1).execute()


def book():
    """
    Calls the relevant functions to book the patient into an event/slot.
    """
    update_calendar.update_calendars()
    campus = info.get_campus()
    if campus != None:
        if campus == 'jhb':
            data = display_calendar.get_jhb_data()
        elif campus == 'cpt':
            data = display_calendar.get_cpt_data()
        start = info.get_start_time()
        email = info.get_email()
        if start != False:
            if is_volunteer_available(data, start, email):
                volunteer_email = get_volunteer_email(data, start)
                event_id = get_event_id(data, start)
                service = token_tool.load_app_token()
                calendar_id = info.get_calendar_id()
                topic = get_topic(data, start)
                random_id = create_random_id()
                add_patient(service, calendar_id, event_id, \
                    volunteer_email, email, random_id)
                print(''' Successfully booked slot with following details:\n
\tCampus   : {}
\tDate     : {}
\tTime     : {}
\tTopic    : {}
\tVolunteer: {}'''.format(campus, start[:10], start[11:16], topic, volunteer_email))
            else:
                print(error_span+
                'The time slot at {} {} is not available to volunteer.'\
                .format(start[:10], start[11:16]))
                print('\n\tPlease use \33[100m./cc calendar\33[0m \
check calendar.')