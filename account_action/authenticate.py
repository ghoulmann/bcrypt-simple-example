import shelve
from getpass import getpass
#from user import User
import json
def authenticate():
    with open('config.json') as config:
        persistence = json.load(config)
        persistence = persistence['shelve']['file']
    authenticated = False
    count = 0
    while authenticated == False and count <= 2:
        db = shelve.open(persistence)
        uname = input("Username: ")
        if db[uname]:
            print("username matches")
            user = db[uname]

            password = getpass("Password: ")
            #password = password


            if user.checkpw(password):

                print("You are in...buckle up.")
                authenticated = True
                #return True
                #except:
                #    print(authenticated)
            else:
                count += 1
                print("Please try again.")


        else:
            print("User not found")
            count += 1
            authenticated = False

    if count >= 2:
        #clear()
        print("Sorry, you've exceed the permitted tries. Now exiting.")
    db.close()