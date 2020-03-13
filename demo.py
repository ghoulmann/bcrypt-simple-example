from account import auth, create
from util import rain
def main():

    if (input("Do you want to create a new account? ")[0].lower() == 'y'):
        print("creating account".upper())
        create()

    else:
        print("authenticating".upper())
        authenticated = auth()
        if authenticated:
            rain(80, 80)

if __name__ == "__main__":
    main()