import random

class Error500(Exception):
    pass

class UsernameAlreadyExistsError(Exception):
    pass

class WrongCredentialsError(Exception):
    pass

class Server:

    def __init__(self):
        self.registeredAccounts = {}

    def get_central_news_page(self):
        
        i = random.randint(1, 10)

        if i > 1:
            return "NEWS PAGE. [showing news...]"
        
        raise Error500()

    def register(self, username : str, password : str):

        i = random.randint(0, 100)
        if i == 100:
            raise Error500()

        if username not in self.registeredAccounts.keys():
            self.registeredAccounts.update( { username : password} )
            return f"Successful register! Welcome, {username}."
        else:
            raise UsernameAlreadyExistsError()

    def login(self, username : str, password : str):

        if username in self.registeredAccounts.keys():
            
            if self.registeredAccounts[username] == password:
                return f"Successful login. Good to see you again, {username}!"
            
        else:
            raise WrongCredentialsError()
