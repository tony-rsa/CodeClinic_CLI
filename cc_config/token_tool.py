import os
import pickle
from pathlib import Path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


hidden_dir = str(Path.home())+'/.codeclinic/token/'
error_span = "\n \033[93m[Error] \033[91m->\033[0m "

SCOPES = 'https://www.googleapis.com/auth/calendar'


def check_email(creds):
    """
        This function checks if the users email is a wethinkcode email address.
        :param creds: the users google calendar creds.
        :return True, user_email: if the email is valid.
        :return False, "": if the  email is not valid.
    """
    service = build('calendar', 'v3', credentials=creds)
    results = service.calendarList().get(calendarId='primary').execute()
    if not "wethinkcode.co.za" in results["id"]:
        print(error_span+"Please use your wethinkcode email address!")
        return False, ""
    return True, results["id"]


def create_token(token_name):
    """
        This function creates a new token.
        :param token_name: the name to give the token.
        :return True. user_email: if successful.
        ::return False, "": if not successful.
    """
    flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    result = check_email(creds)
    if os.path.exists(hidden_dir) and result[0]:
        with open(hidden_dir+token_name+'.pickle', 'wb') as token:
            pickle.dump(creds, token)
        token.close()

    if os.path.exists(hidden_dir+token_name+'.pickle'):
        return True, result[1]
    return False, ""


def load_token(token_name):
    """
        This function Loads a token
        :param token_name: to name of the token to be loadded
        :return service: google api creds build into service
        :returns None: if faild
    """
    creds = None
    if os.path.exists(hidden_dir+token_name+'.pickle'):
        with open(hidden_dir+token_name+'.pickle', 'rb') as token:
            creds = pickle.load(token)
        token.close()
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('credentials/app_token.pickle', 'wb') as token:
            pickle.dump(creds, token)
        token.close()

    if creds != None:
        return build('calendar', 'v3', credentials=creds)
    return None


def load_app_token():
    """
        This function Loads a token
        :param token_name: to name of the token to be loadded
        :return service: google api creds build into service
        :returns None: if faild
    """
    creds = None
    try:
        if os.path.exists('credentials/app_token.pickle'):
            with open('credentials/app_token.pickle', 'rb') as token:
                creds = pickle.load(token)
            token.close()

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('credentials/app_token.pickle', 'wb') as token:
                pickle.dump(creds, token)
            token.close()

        if creds != None:
            return build('calendar', 'v3', credentials=creds)
    except:
        return None


def get_email(token_name):
    """
        This function uses the users token to get the users email
        :param token_name: the users token name
        :return user_email: the users email as string
    """
    service = load_token(token_name)
    user_email = service.calendarList()\
                            .get(calendarId='primary').execute()["id"]
    return user_email


def verify_token(token_name):
    """
        This function checks if user token is connected to users calendar
        :param token_name: the users token name
        :return True: is user is conncted, False if not
    """
    service = load_token(token_name)
    results = service.calendarList().get(calendarId='primary').execute()
    if results['primary'] == True:
        print("\t \033[92m->\033[0m Connection to the primary calendar\
 for "+results['id']+" was successful.")
        return True
    print("\033[93m[Error] \033[91m->\033[0m \
Connection attempt failed! try again or register")
    return False


def delete_token(token_name):
    """
        This function deletes the users token
        :param token_name: the users token name
        :return True/False: True if successful, False if not.
    """
    if os.path.exists(hidden_dir+token_name+'.pickle'):
        os.remove(hidden_dir+token_name+'.pickle')
        return True
    return False