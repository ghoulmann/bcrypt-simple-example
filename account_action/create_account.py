import shelve
from user import User
from getpass import getpass
from pw_validator import main as pw_is_valid
import json

def create_account():
    with open('config.json') as config:
        persistence = json.load(config)
        persistence = persistence['shelve']['file']

    uconfirm = False
    pconfirm = False
    #count = 0

    #process username and create user
    while uconfirm == False:
        uname = input("Please enter a username: ")
        confirmed = input("You've chosen \'%s\' - are you sure (y or n)? " % (uname))
        if confirmed[0].lower() == 'y':
            with shelve.open(persistence) as db:
                if uname in list(db.keys()):
                    print("That username is taken. Please choose another.")
                    uconfirm = False
                else:
                    uconfirm = True
                    user = User(uname.lower())
                    print("Username confirmed.")

    while pconfirm == False:
        pass1 = getpass("Please enter a password: ")
        if pw_is_valid(pass1):
            pass2 = getpass("Please confirm the password: ")
            if pass1 == pass2:
                pconfirm = True

            else:
                pconfirm = False
        else:
            pconfirm = False




    if user.hashpw(pass1) == True:

        with shelve.open(persistence) as db:
            db[user.username] = user



    print("Your account has been created successfully.")
    return True
