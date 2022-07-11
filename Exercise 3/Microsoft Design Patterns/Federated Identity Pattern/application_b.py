class ApplicationB:

    def __init__(self):
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