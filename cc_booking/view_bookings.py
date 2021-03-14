from cc_user import user
from cc_booking import info, booking, volunteer
from cc_calendar import update_calendar, display_calendar

std_pointer = " \033[92m->\033[0m "

def view_bookings():
    """
    Retrieves the booking information which the user is involved in from the dictionary
    and prints out the details
    """
    print(std_pointer+"Downloading your bookings..\n")
    count = 0
    update_calendar.update_calendars()
    email = info.get_email()
    campus = info.get_campus()
    print("\t  Use \33[100m./cc cancel_booking [event id]\33[0m \
to cancle a booking.")
    print("\t  Use \33[100m./cc cancel_volunteer [event id]\33[0m\
 to stop volunteering.\n")
    
    if campus == 'jhb':
        data_dict = display_calendar.get_jhb_data()
    elif campus == 'cpt':
        data_dict = display_calendar.get_cpt_data()
    
    print_flg = True
    for i in data_dict:
        if data_dict[i]['volunteer'] == email:
            count += 1
            if print_flg:
                print(' You have volunteered for the following slot(s):')
                print_flg = False
            print('''\n\tCampus     : {}
\tEvent ID   : \33[100m{}\33[0m
\tDate       : {}
\tTime       : {}
\tTopic      : {}
\tPatient    : {}'''\
    .format(campus, data_dict[i]['id'], i[:10], i[11:16],\
     data_dict[i]['topic'], data_dict[i]['patient']))
    
    print_flg = True
    for i in data_dict:
        if data_dict[i]['patient'] == email:
            count += 1 
            if print_flg:
                print('\n\n You are a patient for the following slot(s):')
                print_flg = False
            print('''\n\tCampus     : {}
\tEvent ID   : \33[100m{}\33[0m
\tDate       : {}
\tTime       : {}
\tTopic      : {}
\tVolunteer  : {}'''\
    .format(campus, data_dict[i]['id'], i[:10], i[11:16], \
        data_dict[i]['topic'], data_dict[i]['volunteer']))
    print("\n"+std_pointer+f"You have {count} bookings.")
    return True

