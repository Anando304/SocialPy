#  @file main.py
#  @author Anando Zaman
#  @brief Main controller class used to navigate the application
#  @date February 10, 2021
from Firebase.firebase_creds import firebase_class
from Firebase.Authentication import *
from CommandParser.CommandParser import *


''' Create connection to DB '''
firebase = firebase_class()
# Get database instance
db = firebase.get_db()


''' start-up screen '''
startup = ''' _    _      _                            _          _____            _       _______      
| |  | |    | |                          | |        /  ___|          (_)     | | ___ \     
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   \ `--.  ___   ___ _  __ _| | |_/ /   _ 
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   `--. \/ _ \ / __| |/ _` | |  __/ | | |
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | /\__/ / (_) | (__| | (_| | | |  | |_| |
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  \____/ \___/ \___|_|\__,_|_\_|   \__, |
                                                                                      __/ |
                                                                                     |___/ '''
exit_text = ''' _____ _                 _           __                       _               _____            _       _______      _ 
|_   _| |               | |         / _|                     (_)             /  ___|          (_)     | | ___ \    | |
  | | | |__   __ _ _ __ | | _____  | |_ ___  _ __   _   _ ___ _ _ __   __ _  \ `--.  ___   ___ _  __ _| | |_/ /   _| |
  | | | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| | | | / __| | '_ \ / _` |  `--. \/ _ \ / __| |/ _` | |  __/ | | | |
  | | | | | | (_| | | | |   <\__ \ | || (_) | |    | |_| \__ \ | | | | (_| | /\__/ / (_) | (__| | (_| | | |  | |_| |_|
  \_/ |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|     \__,_|___/_|_| |_|\__, | \____/ \___/ \___|_|\__,_|_\_|   \__, (_)
                                                                       __/ |                                   __/ |  
                                                                      |___/                                   |___/   '''
print(startup + "\n Type 'su' to signup OR 'si' to signin\n If you forgot your email, type 'reset'.")

''' Authenticate user '''
while firebase.get_user_instance() == None:
    input_ = ""
    # filter out any incompatible commands
    while input_.strip().lower() not in ('su', 'si', "reset"):
        sys.stdout.write(">")
        input_ = input()
        if input_.strip() == 'exit':
            print(exit_text)
            sys.exit()
        if input_.strip() not in ('su', 'si', "reset"):
            print("Sorry, that is not a valid input. Type 'su' to signup OR 'si' to signin")

    # Authentication module initialization
    Authenticate = Authentication(firebase, db)

    # Registration
    if input_.strip() == 'su':
        Authenticate.register()

    # Login
    '''
    Sample account credentials:
    anando@gmail.com 123456789
    yuvirayz@gmail.com 123456789
    woodsg1@mcmaster.ca 123456789
    '''
    if input_.strip() == 'si':
        Authenticate.login()

    if input_.strip() == 'reset':
        Authenticate.password_reset()


''' Post-Authentication stage: Interaction with the application'''
print("\nWelcome back, " + firebase.get_username() + "!")
print("Type 'help' if you would like to find out about the various commands!\nYou can also type 'exit' to quit.")
command = ""
running = [True]
command_parser = CommandParser(running, firebase, db)
while running[0]:
    sys.stdout.write(">")
    command = input()
    command_parser.parseCommand(command)



