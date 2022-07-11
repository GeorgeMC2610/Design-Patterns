from application_a import ApplicationA
from application_b import ApplicationB
from application_c import ApplicationC

class Auth:
    
    def __init__(self):
        self.registered_accounts = {}
        self.application_a = ApplicationA()
        self.application_b = ApplicationB()
        self.application_c = ApplicationC()

    def login(self, username, password):
        if username not in self.registered_accounts.keys():
            print("Wrong credentials.") 
        
        if self.registered_accounts[username] != password:
            print("Wrong credentials.")
        
        print(f"Welcome back, {username}!")
    
    def register(self, username, password):
        if username in self.registered_accounts.keys():
            print("Username already exists.")
        
        print("Encrypting passwords...")
        self.registered_accounts.update( {username : password} )

        self.application_a.register(username, password)
        self.application_b.register(username, password)
        self.application_c.register(username, password)

        print(f"Welcome! Nice to have you, {username}. You have now access to all applications!")

    def useful_function_a(self, username, password):

        self.application_a.login(username, password)
        self.application_a.useful_function()

    def useful_function_b(self, username, password):

        self.application_a.login(username, password)
        self.application_a.useful_function()

    def useful_function_c(self, username, password):

        self.application_a.login(username, password)
        self.application_a.useful_function()
