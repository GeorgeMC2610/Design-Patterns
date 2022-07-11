### RETRY DESIGN PATTERN

from server import Server
from retry import Retry

# this pattern is showing an app (main.py) trying to connect to a server.
# if the operation is to load a news page, the pattern is going to let the app retry several times before it fails.
# if the operation is to give bad credentials, it's not going to let it happen more than once.

print("RETRY DESIGN PATTERN\n\n")

server1 = Server()
retry_pattern = Retry(server1)


print("Type '1' to see the central news page.")
print("Type '2' to register.")
print("Type '3' to login.")
print("Type '0' to exit.\n")

actions = {
    '1' : retry_pattern.retry_news_page,
    '2' : retry_pattern.retry_register,
    '3' : retry_pattern.retry_login
}

while True:
    user_input = input("Select an action --> ")

    if user_input == '0':
        break

    while user_input not in actions:
        user_input = input("Wrong action. Try again --> ")

    if user_input == '2' or user_input == '3':
        input_username = input("Enter Username --> ")
        input_password = input("Enter Password --> ")
        print(actions[user_input](input_username, input_password))
    else:
        print(actions[user_input]())