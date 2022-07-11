from server import Server, Error500, WrongCredentialsError, UsernameAlreadyExistsError

class Retry:

    def __init__(self, server : Server):
        self.server = server

    def retry_news_page(self):

        tries = 0
        while True:

            try:
                return self.server.get_central_news_page()
            except:
                tries += 1
                print(f"Failed attempt. (Tries: {tries})")

                if (tries > 5):
                    return "Too many failed attempts. Server is not responding."

    def retry_register(self, username, password):

        tries = 0
        while True:

            try:
                return self.server.register(username, password)
            except Error500:
                tries += 1
                print(f"Failed attempt. (Tries: {tries})")

                if (tries > 5):
                    return "Too many failed attempts. Server is not responding."
            except UsernameAlreadyExistsError:
                return "The Username you picked already exists."

    def retry_login(self, username, password):

        tries = 0
        while True:

            try:
                return self.server.login(username, password)
            except Error500:
                tries += 1
                print(f"Failed attempt. (Tries: {tries})")

                if (tries > 5):
                    return "Too many failed attempts. Server is not responding."
            except WrongCredentialsError:
                return "Wrong Username and/or Password."