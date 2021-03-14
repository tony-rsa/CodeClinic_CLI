import os
import sys
import datetime
import configparser
from cc_config import config

error_span = "\n \033[93m[Error] \033[91m->\033[0m "
std_pointer = " \033[92m->\033[0m "

home_dir = os.path.expanduser('~')
hidden_dir = os.path.join(home_dir, '.codeclinic')
config_file = os.path.join(hidden_dir, 'config.ini')

def get_email():
    """
    Gets the users email address from the config file
    return: user email
    """
    email = None
    try:
        user_name = config.get_logged()
        email = config.get_user_info(user_name, "user_email")
    except:
        print(error_span+'Please Login or Register.')
    return email


def get_campus():
    """
    Gets the user's campus(jhb/cpt) from config file
    return: jhb or cpt
    """
    campus = {"1" : "cpt", "2" : "jhb"}

    try:
        user_name = config.get_logged()
        campus = campus[config.get_user_info(user_name, "campus_index")]
    except:
        print(error_span+'Please Login or Register.')
    return campus


def get_calendar_id():
    """
    Returns calendar id for creating and updating events
    return: calendar id
    """
    campus = get_campus()

    if campus == 'jhb':
        return 'r13l5vvegs28cnlq58u863vg74@group.calendar.google.com'
    elif campus == 'cpt':
        return 'gsuf19ff4dvn8uo2fdan5ct8q4@group.calendar.google.com'
    else:
        return None
    

def get_start_time():
    """
    Gets the date and time from command line
    return: start time of event or False if not a valid date/time
    """
    now = datetime.datetime.now()
    delta = datetime.datetime.now() + datetime.timedelta(days=10)
    if sys.argv[1] == 'volunteer' or sys.argv[1] == 'book':
        if len(sys.argv) >= 4:
            d = sys.argv[2]
            t = sys.argv[3]
        try:
            ds = d.split('-')
            year = int(ds[0])
            month = int(ds[1])
            day = int(ds[2])
        except:
            print(error_span+'Please enter valid date.')
            return False
        try:
            ts = t.split(':')
            hour = int(ts[0])
            minute = int(ts[1])
        except:
            print(error_span+'Please enter valid time.')
            return False
        if (hour in range(7, 18)) and (minute == 00 or minute == 30):
            try:
                date_time = datetime.datetime(year, month, day,\
                                                 hour, minute, 00)
            except:
                print(error_span+"Please enter valid date.")
                return False
        else:
            print(error_span+'Please enter time between 07:00 and 17:30 in\
 30 minute intervals only.')
            return False
        if now < date_time < delta:
            return str(date_time.isoformat() + '+02:00')
        else:
            print(error_span+'Date out of range.')
            print('\n\tPlease enter date within next 10 days.')
            return False
    

def get_end_time(start):
    """
    adds 30 minutes to start time to get end time.
    parameters: start: start time of event.
    return: end time of event
    """
    delta = datetime.timedelta(minutes=30)
    s, tz = start.split('+')
    s = datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')
    end_time = s + delta
    return end_time.isoformat() + '+02:00'
    

def get_topic():
    """
    Gets the topic from command line.
    return: topic
    """
    if sys.argv[1] == 'volunteer':
        if len((sys.argv)) >= 5:
            topic = sys.argv[4]
        else:
            topic = 'Anything goes'
    return topic


def get_event_id():
    """
    Gets the event id from command line
    return: event id
    """
    if sys.argv[1] == 'cancel_booking' or sys.argv[1] == 'cancel_volunteer':
        event_id = sys.argv[2]
    return event_id