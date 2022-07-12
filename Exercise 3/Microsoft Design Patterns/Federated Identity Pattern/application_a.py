import random

class ApplicationA:

    def __init__(self):
        ApplicationA.Tokens = []
        self.registered_accounts = {}

    def generate_token(self) -> str:
        
        symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        token = ''.join([symbols[random.randint(0, len(symbols)-1)] for i in range(20)])
        ApplicationA.Tokens.append(token)
        return token
    
    def useful_function_a(self, token):

        if token not in ApplicationA.Tokens:
            return "This action cannot be done!"
        
        return "Useful function from A."