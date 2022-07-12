from email.mime import application
import random

class ApplicationA:

    def __init__(self):
        ApplicationA.Tokens = []
        self.registered_accounts = {}

    def login(self, username, password):
        if username not in self.registered_accounts.keys():
            return "Wrong credentials."
        
        if self.registered_accounts[username] != password:
            return "Wrong credentials."
        
        return f"Welcome back, {username}!"
    
    def register(self, username, password):
        if username in self.registered_accounts.keys():
            return "Username already exists."
        
        self.registered_accounts.update( {username : password} )
        return f"Welcome! Nice to have you, {username}."

    def generate_token(self) -> str:
        
        symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        token = ''.join([symbols[random.randint(0, len(symbols)-1)] for i in range(20)])
        ApplicationA.Tokens.append(token)
        return token
    
    def useful_function_a(self, token):

        if token not in ApplicationA.Tokens:
            return "This action cannot be done!"
        
        return "Useful function from A."

app = ApplicationA()

print(app.generate_token())