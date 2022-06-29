class Student:

    def __init__(self, name) -> None:
        self.name = name

    def introduction(self):
        print(f"Hello! I'm Student {self.name}.")