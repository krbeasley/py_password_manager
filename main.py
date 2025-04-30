#!./.ppm_venv/bin/python3
from Terminal.Terminal import Terminal
from Application import Application
import argparse

parser = argparse.ArgumentParser()  # Initialize the argument parser 
terminal = Terminal()               # Initialize the terminal window handler
app = Application()                 # Initialize the application instance

# Accepted arguments
parser.add_argument('-n', help="Create a new password entry.", action=argparse.BooleanOptionalAction, default=False)
parser.add_argument('-f', help="Force action to take place. Silence all warnings.", action=argparse.BooleanOptionalAction, default=False)
parser.add_argument('-u', help='Specify a username (or email) for the account.', default=None)
parser.add_argument('-d', help='Specify a domain (website) for the account.', default=None)
parser.add_argument('-p', help='Specify a password for the account.', default=None)
parser.add_argument('-v', help='Specify verbose output. Default off', action=argparse.BooleanOptionalAction, default=False)

if __name__ == "__main__":
    args = parser.parse_args()
    app.initialize(args.n, args.f, args.v)

    username = args.u
    domain = args.d
    password = args.p

    match app.action:
        case "create":
            pass
            # get the info for the new credentials
            terminal.write("This is a test", terminal.colors.WARNING)

            # create new credentials object

            # save the new credentials
            
        case "lookup":
            pass
