import os
import json
import pickle
import warnings
from cc_config import token_tool
from datetime import datetime, timedelta

warnings.simplefilter(action='ignore', category=FutureWarning)

home_dir = os.path.expanduser('~')
clinic_dir = os.path.join(home_dir, 'codeclinic')
calendar_jhb_file = os.path.join(clinic_dir, 'calendar_data_jhb.json')
calendar_cpt_file = os.path.join(clinic_dir, 'calendar_data_cpt.json')

calendar_dictj = {}
calendar_dictc = {}

def create_calendar_files():
    """
    Creates a directory and data files in the home directory if they do not already exist.
    """
    if not os.path.exists(clinic_dir):
        os.mkdir(clinic_dir)
    if not os.path.isfile(calendar_jhb_file):
        with open(calendar_jhb_file, 'w') as file:
            pass
    if not os.path.isfile(calendar_cpt_file):
        with open(calendar_cpt_file, 'w') as file:
            pass
    return True


def update_calendar_jhb(service):
    """
    Gets next 7 days of events from Google jhb calendar id and returns list
    parameters: service: the service from the token to access Google calendar
    returns: events_jhb: list of events from Google calendar
    """
    now = datetime.now().isoformat() + '+02:00'
    delta = datetime.now() + timedelta(days=10)
    max_time = delta.isoformat() + 'Z'
    events_result_jhb = service.events()\
    .list(calendarId='r13l5vvegs28cnlq58u863vg74@group.calendar.google.com', 
                            timeMin=now, timeMax=max_time, singleEvents=True, 
                        orderBy='startTime').execute()
    return events_result_jhb.get('items', [])


def save_data_jhb(events):
    """
    Saves a dictionary of events to jhb json data file
    parameters: events: list of events
    return: boolean value on whether data was successfully saved
    """
    global calendar_dictj

    for event in events:
        patient = None
        event_id = str(event['id'])
        start = str(event['start'].get('dateTime', \
            event['start'].get('date')))
        volunteer = str(event['attendees'][0]['email'])
        if len(event['attendees']) == 2:
            patient = str(event['attendees'][1]['email'])
        try:
            topic = str(event['summary'])
        except:
            topic = 'Anything Goes'

        calendar_dictj[start] = {}
        calendar_dictj[start] = {
            'id' : event_id,
            'topic' : topic,
            'volunteer' : volunteer,
            'patient' : patient}
    try:
        with open(calendar_jhb_file, 'w') as calendar_data:
            json.dump(calendar_dictj, calendar_data)
        return True
    except:
        return False


def update_calendar_cpt(service):
    """
    Gets next 7 days of events from Google cpt calendar id and returns list
    parameters: service: the service from the token to access Google calendar
    returns: events_jhb: list of events from Google calendar
    """
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    delta = datetime.utcnow() + timedelta(days=10)
    max_time = delta.isoformat() + 'Z'
    events_result_cpt = service.events()\
     .list(calendarId='gsuf19ff4dvn8uo2fdan5ct8q4@group.calendar.google.com', 
                            timeMin=now, timeMax=max_time, singleEvents=True,
                            orderBy='startTime').execute()
    return events_result_cpt.get('items', [])


def save_data_cpt(events):
    """
    Saves a dictionary of events to jhb json data file
    parameters: events: list of events
    return: boolean value on whether data was successfully saved
    """
    global calendar_dictc

    for event in events:
        patient = None
        event_id = str(event['id'])
        start = str(event['start'].get('dateTime',\
             event['start'].get('date')))
        volunteer = str(event['attendees'][0]['email'])
        if len(event['attendees']) == 2:
            patient = str(event['attendees'][1]['email'])
        try:
            topic = str(event['summary'])
        except:
            topic = 'Anything Goes'
        
        calendar_dictc[start] = {}
        calendar_dictc[start] = {
            'id' : event_id,
            'topic' : topic,
            'volunteer' : volunteer,
            'patient' : patient}
    try:
        with open(calendar_cpt_file, 'w') as calendar_data:
            json.dump(calendar_dictc, calendar_data)
        return True
    except:
        return False


def update_calendars():
    """
    Calls the relevant functions to update the data files with latest info
    """
    create_calendar_files()
    service = token_tool.load_app_token()
    events_jhb = update_calendar_jhb(service)
    save_data_jhb(events_jhb)
    events_cpt = update_calendar_cpt(service)
    save_data_cpt(events_cpt)
    
