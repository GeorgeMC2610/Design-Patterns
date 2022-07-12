import random

class ApplicationC:

    def __init__(self):
        self.registered_accounts = {}

    def generate_token(self) -> str:
    
        symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        token = ''.join([symbols[random.randint(0, len(symbols)-1)] for i in range(20)])
        ApplicationC.Tokens.append(token)
        return token
    
    def useful_function_c(self, token):

        if token not in ApplicationC.Tokens:
            return "This action cannot be done!"
        
        return "Useful function from C."