# ASSUMING WE HAVE AN APPLICATION (main.py)
# we want to have a central authentication and authorization service to access several applications
# so create several classes to do so.

import sys
from auth import Auth

auth1 = Auth()


print("=== FEDERATED IDENTITY PATTERN ===\n\n")

print("AVAILABLE ACTIONS:")
print("Press '0' to exit.")
print("Press '1' to login.")
print("Press '2' to register.\n")


available_actions = {
    '1' : auth1.login,
    '2' : auth1.register
}

while True:
    action = input("Select an action --> ")

    if action == '0':
        sys.exit()

    while action not in available_actions:
        action = input("Wrong action, please enter one from the available ones --> ")

    input_username = input("Provide your username --> ")
    input_password = input("Provide your password --> ")

    if available_actions[action](input_username, input_password) and action == '1':
        pass
    else:
        continue

    while True:

        other_available_actions = {
            'a' : auth1.connect_to_application_a,
            'b' : auth1.connect_to_application_b,
            'c' : auth1.connect_to_application_c
        }

        other_action = input(f"{input_username}, please select an application (a, b or c) --> ")

        while other_action not in other_available_actions:
            other_action = input("Wrong application, please enter one from the available ones --> ")
        
        other_available_actions[other_action]()
        sys.exit()