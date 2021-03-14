import os
import sys
import json
import datetime
from cc_booking import info
from cc_calendar import update_calendar
from beautifultable import BeautifulTable

std_pointer = "\033[92m->\033[0m "
error_span = "\033[93m[Error] \033[91m->\033[0m "
error_spanre = "\033[92m[ErrorResolved] \033[91m->\033[0m "

home_dir = os.path.expanduser('~')
clinic_dir = os.path.join(home_dir, 'codeclinic')
calendar_jhb_file = os.path.join(clinic_dir, 'calendar_data_jhb.json')
calendar_cpt_file = os.path.join(clinic_dir, 'calendar_data_cpt.json')

def get_jhb_data():
    """
    Retrieves the data from jhb json file
    returns: jhb_dict: dictionary of events from json file
    """
    try:
        with open(calendar_jhb_file, 'r') as json_file:
            jhb_dict = json.load(json_file)
    except:
        jhb_dict = {}
    return jhb_dict


def get_cpt_data():
    """
    Retrieves the data from cpt json file
    returns: cpt_dict: dictionary of events from json file
    """
    try:
        with open(calendar_cpt_file, 'r') as json_file:
            cpt_dict = json.load(json_file)
    except:
        cpt_dict = {}
    return cpt_dict


def get_number_of_days():
    """
    Gets the number of days to be displayed on calendar
    return: number of days as int
    """
    if sys.argv[1] == 'calendar':
        if len(sys.argv) == 3:
            try:
                no_of_days = int(sys.argv[2])
            except:
                print(error_span+
                'Please enter an integer between 1 and 10 inclusive.')
                print(error_spanre+'Number of days has defaulted to 7.\n')
                no_of_days = 7
            if 1 <= no_of_days <= 10:
                return no_of_days
            else:
                print(error_span+
                'Please enter an integer between 1 and 10 inclusive.')
                print(error_spanre+'Number of days has defaulted to 7.\n')
                return 7
        else:
            no_of_days = 7
    return no_of_days


def create_slot_dict():
    """
    Creates an empty dictionary of all timeslots for 7 days as keys
    returns: time_slots_dict: dictionary of time slots
    """
    time_slots_dict_empty = {}
    date = datetime.date.today()
    d = 0
    while d != 10:
        time = datetime.datetime(1, 1, 1, 7, 00, 00)
        s = 0
        while s != 22:
            date_time = datetime.datetime.combine(date, time.time())
            time_slots_dict_empty[str(date_time.isoformat() + '+02:00')] = ''
            time = time + datetime.timedelta(minutes=30)
            s += 1
        date = date + datetime.timedelta(days=1)
        d += 1
    return time_slots_dict_empty


def populate_slots_dict(time_slots_dict, events):
    """
    Populates the time slots dictionary with outputs depending on the events details.
    parameters: time_slots_dict: empty dictionary of timesots
                events: list of events
    returns: time_slots_dict: dicionary of outputs for each time slot
    """
    red = '\033[91m'
    green = '\033[32m'
    bold = '\033[1m'
    reset = '\033[0m'

    for i in events:
        if events[i]['volunteer'] is not None and \
                                events[i]['patient'] is not None:
            output = red + bold + 'Booked' + reset
        elif events[i]['volunteer'] is not None and \
                                    events[i]['patient'] is None:
            output = green + bold + events[i]['topic'] + reset
        else:
            output = ''
        time_slots_dict[i] = output
    return time_slots_dict
            

def create_table(time_slot_dict, no_of_days):
    """
    Creates a calendar table to represent the data from the time slots dictionary
    parameters: time_slot_dict: dictionary with timeslots as keys and outputs as values
    returns: cal: the calendar in table format
    """
    bold = '\033[1m'
    reset = '\033[0m'
    slots = []
    days = ['']
    time = ['07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
             '10:00', '10:30','11:00', '11:30', '12:00', '12:30',
             '13:00', '13:30','14:00', '14:30', '15:00', '15:30',
             '16:00', '16:30', '17:00', '17:30']
    
    date = datetime.datetime.now()
    day = date.strftime('%a')
    for i in range(0, 10):
        days.append(bold + '   ' + day + '    ' + str(date)[:10] + reset)
        date = date + datetime.timedelta(days=1)
        day = date.strftime('%a')
    for key in time_slot_dict:
        slots.append(str(time_slot_dict[key]))
    
    cal = BeautifulTable()
    headers = []
    widths = [7]
    for h in range(0, no_of_days + 1):
        headers.append(days[h])
    
    for w in range(0, no_of_days):
        widths.append(12)

    for i in range(0, 22):
        rows = []
        rows.append(time[i])
        for d in range(0, no_of_days):
            rows.append(slots[(d*22)+i])
        cal.rows.append(rows)
    cal.columns.header = headers
    cal.column_widths = widths
    return cal


def print_calendar():
    """
    Calls the relevant functions to print updated calendar
    """
    print(" \033[92m->\033[0m Downloading calendar..\n")
    update_calendar.update_calendars()
    campus = info.get_campus()
    if campus != None:
        if campus == 'jhb':
            data = get_jhb_data()
            print("     ~ Johannesburg\n")
        elif campus == 'cpt':
            data = get_cpt_data()
            print("\t ~ Cape Town\n")
        print("\tUse \33[100m./cc book [date] [time]\33[0m to book a slot.")
        print("\tUse \33[100m./cc volunteer [date] [time] 'topic'\33[0m\
 to volunteer for a slot.\n")
    else:
        print('Please login or register.')
    empty_dict = create_slot_dict()
    event_dict = populate_slots_dict(empty_dict, data)
    no_of_days = get_number_of_days()
    calendar_table = create_table(event_dict, no_of_days)
    print(calendar_table)

