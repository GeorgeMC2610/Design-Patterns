class AnimalRegister:

    def __init__(self, name, animal) -> None:
        self.name = name
        self.animal = animal

    def register(self):
        print(f"Registered animal {self.animal} with name {self.name}.")