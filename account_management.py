from getpass import getpass
import password_hashing
import time
import db_management

username_db = {}
username = ""
username_input = ""
password_count = 0
password_attempts = 3
password_timeout = 60
password_output = ""
firstname_input = ""
lastname_output = ""
email_address_output = ""
pwdHistoryLimit = 12



def main():
    print("")

def forgot_password():
    print("")


def forgot_username():
    print("")



        
        
# Create account functions
def create_username_section(database):
    while True:
        # Queue up usernames in directory for reference
        username_input = input("Username: ")
        database_lst = list(database)
        if username_input in database_lst:
            print("The username you have selected is currently in use. Please try again:")
            continue
        else:
            print("Username is available. Please create a password to use.")
            time.sleep(1)
            return username_input


def create_password_section():
    # Create Password
    create_password = password_hashing.encrypt_password(getpass("Enter password: "))
    verify_password = getpass("Enter password again: ")
    if password_hashing.verify_passwords(verify_password, create_password) != True:
            while True:
                # If the first password equals the second password display that the password matches then
                # continue to the next part
                if password_hashing.verify_passwords(verify_password, create_password) == True:
                    print("Password matches")
                    empty_List = ["" for i in range(pwdHistoryLimit)]
                    empty_List[0] = create_password
                    return  create_password
                else:
                    # If the passwords do not match, have the user retry until password matches
                    print("Password does not match. Please retry")
                    create_password = password_hashing.encrypt_password(getpass("Enter password: "))
                    verify_password = getpass("Enter password again: ")
                    continue
    else:
        print("Password matches")
        empty_List = ["" for i in range(pwdHistoryLimit)]
        empty_List[0] = create_password
        return empty_List


def enter_first_name():
    firstname_input = input("Please type your First Name:")
    # print(firstname_output)
    return firstname_input


def enter_last_name():
    lastname_input = input("Please type your Last Name:")
    lastname_output = lastname_input
    # print(lastname_output)
    return lastname_output


def enter_email_address():
    email_address = input("Please enter your email address: ")
    email_address_verification = input("Please re-enter your email address: ")
    if email_address == email_address_verification:
        print("E-mail Addresses are matched.")
        return email_address
    else:
        print("E-mail Addresses are not matching. Please re-enter your email address.")
        enter_email_address()


# Login Functions
def db_username_check(database):
    database_lst = list(database)
    # print(username_db)
    username_input = str(input("Please enter your username: "))
    if username_input in database_lst:
        return db_password_check(username_input, database)
    elif username_input == "exit" or username_input == "Exit":
        return
    else:
        print("The username you have entered is incorrect")
        db_username_check(database)


def db_password_check(username, database):
    while True:
        user_password = getpass("Please enter your password:")
        userinfo_grab = database.get(username)
        password_List = userinfo_grab.get('Password')
        password_grab = password_List[0]
        if password_hashing.verify_passwords(user_password, password_grab) == True:
            return username
        else:
            print("Incorrect Password")
            global password_count
            password_count += 1
            if password_count == password_attempts:
                print("Too many attempts detected")
                time.sleep(password_timeout)
                db_username_check(database)
            else:
                print("")
            continue


#   Individual Account Management


def usernameChange(username, database):
    user_password = input("Please enter your password to verify that you would like to change your username: ")
    password_grab = database.get(username).get('Password')
    if password_hashing.verify_passwords(user_password, password_grab) == True:
        newUserName = input("Please enter a username that you would like to change to: ")

def usernameIdentity(username, database):
    print("This process will allow you to change the capitolization of your username. You can not add or remove any characters from your username.")
    modified_username = input("Please enter the username you would like to modify to: ")
    if username.lower() == modified_username.lower():
        pass


def passwordUpdateList(username):
    newPwdList = ["" for i in range(pwdHistoryLimit)]
    database = db_management.load_userdb()
    oldPwd = getpass("Please enter old password: ")
    if password_hashing.verify_passwords(oldPwd, database[username]["Password"][0]) == True:
        pwd = create_password_section() 
        oldPwdList = database[username]['Password']
        #   Rotates password for chronological storage
        newPwdList[0], newPwdList[1], newPwdList[2], newPwdList[3], newPwdList[4], newPwdList[5], newPwdList[6], newPwdList[7], newPwdList[8], newPwdList[9] = pwd[0], oldPwdList[0], oldPwdList[1], oldPwdList[2], oldPwdList[3], oldPwdList[4], oldPwdList[5], oldPwdList[6], oldPwdList[7], oldPwdList[8]
        db_management.password_to_db(newPwdList, username)    
    else:  
        passwordUpdateList(username)
   


    