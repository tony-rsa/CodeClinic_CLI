import pexpect
import os.path
from pathlib import Path

def login(pwd1):

    login = pexpect.spawn("./cc login smciwa")
    case = login.expect(["Please enter password"])

    if (case == 0):
        login.sendline(pwd1)
        case = login.expect(["User approved for the next 20 mins.", "User not found, please register."])
        if (case == 0):
            return (True)
        else:
            return (False)
    else:
        return (False)

#print(login("1234"))