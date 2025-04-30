#!./.ppm_venv/bin/python3
from Terminal import Terminal
import argparse

parser = argparse.ArgumentParser()  # Initialize the argument parser 
terminal = Terminal()              # Initialize the terminal window handler

# Application Status
app_status = {
    "force": False,
    "create": False,
    "lookup": True,
    "verbose": True,
}

# Accepted arguments
parser.add_argument('-n', help="Create a new password entry.", action=argparse.BooleanOptionalAction, default=False)
parser.add_argument('-f', help="Force action to take place. Silence all warnings.", action=argparse.BooleanOptionalAction, default=False)
parser.add_argument('-u', help='Specify a username (or email) for the account.', default=None)
parser.add_argument('-d', help='Specify a domain (website) for the account.', default=None)
parser.add_argument('-p', help='Specify a password for the account.', default=None)
parser.add_argument('-v', help='Specify verbose output. Default off', action=argparse.BooleanOptionalAction, default=False)

if __name__ == "__main__":
    args = parser.parse_args()

    # Intialize the application status
    app_status['force'] = args.f
    app_status['create'] = args.n
    app_status['lookup'] = not args.n
    app_status['verbose'] = args.v

    username = args.u
    domain = args.d
    password = args.p

    
