from application_a import ApplicationA
from application_b import ApplicationB
from application_c import ApplicationC

class Auth:

    registered_accounts = {}

    def __init__(self):
        self.application_a = ApplicationA()
        self.application_b = ApplicationB()
        self.application_c = ApplicationC()

    @staticmethod
    def login(username, password) -> bool:

        if username not in Auth.registered_accounts.keys():
            print("Wrong credentials.") 
            return False
        
        if Auth.registered_accounts[username] != password:
            print("Wrong credentials.")
            return False
        
        print(f"Welcome back, {username}!")
        return True
    
    @staticmethod
    def register(username, password) -> bool:

        if username in Auth.registered_accounts.keys():
            print("Username already exists.")
            return False
        
        print("Encrypting passwords...")
        Auth.registered_accounts.update( {username : password} )

        print(f"Welcome! Nice to have you, {username}. You have now access to all applications!")
        return True

    def connect_to_application_a(self):

        token = self.application_a.generate_token()
        print(self.application_a.useful_function_a(token))

    def connect_to_application_b(self):

        token = self.application_b.generate_token()
        print(self.application_b.useful_function_b(token))

    def connect_to_application_c(self):

        token = self.application_c.generate_token()
        print(self.application_c.useful_function_c(token))
