import random
from cc_booking import info
from cc_config import token_tool
from cc_calendar import update_calendar, display_calendar

error_span = "\n \033[93m[Error] \033[91m->\033[0m "

def is_slot_open(data_dict, start_time):
    """
    Checks the dictionary to see if an event exists at specified time.
    parameters: data_dict: dictionary of events
                start_time: the specified start date and time of event
    returns: True if no event exists at specified time
             False if event exists at specified time
    """
    if start_time in data_dict.keys():
        return False
    else:
        return True


def create_event(service, calendar_id, topic, start_time, end_time, email):
    """
    Creates an event and the volunteers specified time.
    parameters: service: google calendar api service
                calendar_id: calendar id of relevant calendar
                topic: the topic the volunteer specified
                start_time: the start time of the event
                end_time: the end time of the event
                email: users email
    """
    event_body = {
        'summary' : topic,
        'start' : {
            'dateTime' : start_time
        },
        'end' : {
            'dateTime' : end_time
        },
        'attendees' : [
            {'email' : email,
            'responseStatus' : 'accepted'}],
    }
    event = service.events().insert(calendarId=calendar_id, body=event_body, \
                        sendUpdates='all', conferenceDataVersion=1).execute()


def volunteer():
    """
    Calls the relevant functions to create volunteers event on calendar.
    """
    update_calendar.update_calendars()
    campus = info.get_campus()
    if campus != None:
        if campus == 'jhb':
            data = display_calendar.get_jhb_data()
        elif campus == 'cpt':
            data = display_calendar.get_cpt_data()
        start = info.get_start_time()
        if start != False:
            if is_slot_open(data, start):
                service = token_tool.load_app_token()
                calendar_id = info.get_calendar_id()
                topic = info.get_topic()
                email = info.get_email()
                end = info.get_end_time(start)
                create_event(service, calendar_id, topic, start, end, email)
                print(''' Successfully created event with following details:\n
\tCampus: {}
\tDate  : {}
\tTime  : {}
\tTopic : {}'''.format(campus, start[:10], start[11:16], topic))
            else:
                print(error_span+
                'The time slot at {} {} is not available to volunteer.'\
                .format(start[:10], start[11:16]))
                print('\n\tPlease use \33[100m./cc calendar\33[0m \
check calendar.')
    
