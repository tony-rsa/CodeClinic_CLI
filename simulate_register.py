import pexpect
import os.path
from pathlib import Path

def del_account():
    hidden_dir = str(Path.home())+'/.codeclinic/config.ini'
    if (os.path.exists(hidden_dir)):
        os.remove(hidden_dir)
    
    if (not os.path.exists(hidden_dir)):
        return(True)
    return (False)


def reg(pwd1, pwd2, pwd3):

    if (del_account()):
        error_span = " \033[93m[Error] \033[91m->\033[0m "
        register = pexpect.spawn("./cc register jhb")
        register.expect(["Please create password"])
        register.sendline(pwd1)
        register.expect(["Please confirm password"])
        register.sendline(pwd2)
        case = register.expect(["Passwords are invalid, try again!"])

        if(case == 0):
            register.sendline(pwd1)
            register.expect(["Please confirm password"])
            register.sendline(pwd3)
            case = register.expect(["Using 'smciwa@student.wethinkcode.co.za' as your email address."])

            if (case == 0):
                return (True)
            else:
                return (False)



# if __name__ == "__main__":
#     del_account()
#     print(reg("1234", "abcd", "1234"))
