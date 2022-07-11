from server import Server

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
                    print("Too many failed attempts. Server is not responding.")
                    break