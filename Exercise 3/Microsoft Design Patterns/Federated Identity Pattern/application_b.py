import random

class ApplicationB:

    def __init__(self):
        self.registered_accounts = {}

    def generate_token(self) -> str:
    
        symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        token = ''.join([symbols[random.randint(0, len(symbols)-1)] for i in range(20)])
        ApplicationB.Tokens.append(token)
        return token
    
    def useful_function_b(self, token):

        if token not in ApplicationB.Tokens:
            return "This action cannot be done!"
        
        return "Useful function from B."