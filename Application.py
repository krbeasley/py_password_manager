from os import path, makedirs
import json

class Application:
    def __init__(self):
        self.force = False
        self.verbose = False
        self.app_path = path.abspath(path.dirname(__file__))
       
    def initialize(self, new_arg, force_arg, verbose_arg):
        """ Finish setting up the application based upon the user's provided arguments.

        Arguments:
        new_arg -- the new argument flag (default False)
        force_arg -- the force argument flag (default False)
        verbose_arg -- the verbose argument flag (default False)
        """
        self.password_file = f"{self.config('default_file_name')}.{self.config('file_extension')}"
        self.force = force_arg
        self.verbose = verbose_arg
        self.action = 'create' if new_arg is True else 'lookup'
        self.credentials = self.getCredentialsList(True) 

    def getConfig(self):
        """Get the application's configuration details as a dict."""
        return {
            "action": self.action,
            "force": self.force,
            "password_file": self.password_file,
            "verbose": self.verbose
        }

    def getCredentialsList(self, refresh = False):
        """Get the application's list of credentials.

        Arguments:
        refresh -- indicate if the application should refresh it's list of credentials (default False)
        """
        if refresh:
            self.setCredentialsList()

        return self.credentials

    def setCredentialsList(self):
        """Set the application's credentials list from the locally stored file. Creates the file if necessary"""
        file_path = path.join(self.app_path, self.password_file)

        # Create a new credentials file if there is none.
        if not path.isfile(file_path):
            with open(file_path, mode='w') as file:
                data = json.dumps([], indent=4)
                file.write(data)

        with open(file_path, mode='r') as file:
            self.credentials = json.loads(file.read())

    def config(self, key):
        """Get a specific config value from the config.ini file
    
        Arguments:
        key -- the config key in question
        """
        config_path = path.join(self.app_path, 'config.ini')

        # Copy the write the default config file if one doesn't exist
        if not path.isfile(config_path):
            with open(config_path, mode='w') as config_file:
                config_file.writelines([
                    "[Settings]",
                    "file_extension=ppm",
                    "default_file_name=user_passwords",
                ])

        config = {}
        with open(config_path, mode='r') as config_file:
            for line in config_file:
                if not line.startswith('[') and not line == "":
                    arr = line.split('=')
                    config[arr[0]] = arr[1].strip()

        return config[key]
