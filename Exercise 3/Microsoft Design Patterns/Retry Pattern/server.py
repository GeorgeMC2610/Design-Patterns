import random

class Server:

    def __init__(self):
        self.registeredAccounts = {}

    def get_central_news_page(self):
        
        i = random.randint(1, 10)

        if i > 4:
            return "NEWS PAGE. [showing news...]"
        
        raise Exception("Error 500")

    def register(self, username : str, password : str):

        if username not in self.registeredAccounts.keys():
            self.registeredAccounts.update( { username : password} )

        else:
            raise Exception("Username already exists.")

    def login(self, username : str, password : str):

        if username in self.registeredAccounts.keys():
            
            if self.registeredAccounts[username] == password:
                return "Successful login."
            
        else:
            raise Exception("Username and/or password wrong.")
