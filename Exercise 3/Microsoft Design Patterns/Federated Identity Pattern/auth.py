from application_a import ApplicationA
from application_b import ApplicationB
from application_c import ApplicationC

class Auth:
    
    def __init__(self):
        self.registered_accounts = {}
        self.application_a = ApplicationA()
        self.application_b = ApplicationB()
        self.application_c = ApplicationC()

    def login(self, username, password) -> bool:
        if username not in self.registered_accounts.keys():
            print("Wrong credentials.") 
            return False
        
        if self.registered_accounts[username] != password:
            print("Wrong credentials.")
            return False
        
        print(f"Welcome back, {username}!")
        return True
    
    def register(self, username, password) -> bool:
        if username in self.registered_accounts.keys():
            print("Username already exists.")
            return False
        
        print("Encrypting passwords...")
        self.registered_accounts.update( {username : password} )

        self.application_a.register(username, password)
        self.application_b.register(username, password)
        self.application_c.register(username, password)

        print(f"Welcome! Nice to have you, {username}. You have now access to all applications!")
        return True

    def useful_function_a(self, username, password):

        self.application_a.login(username, password)
        self.application_a.useful_function()

    def useful_function_b(self, username, password):

        self.application_b.login(username, password)
        self.application_b.useful_function()

    def useful_function_c(self, username, password):

        self.application_c.login(username, password)
        self.application_c.useful_function()
