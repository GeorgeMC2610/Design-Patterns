from IMovable import IMovable
from ILockable import ILockable

class Car(IMovable, ILockable):
    
    def __init__(self) -> None:
        self.locked = False
        self.x = 0
        self.y = 0

    def move(self, x, y):
        
        if self.locked:
            print("Car is locked it cannot move!")
            return

        self.x += x
        self.y += y

        print(f"Successfully moved Car in position {self.x}, {self.y}.")

    def lock(self):
        self.locked = True
        print("Locked the Car.")

    def unlock(self):
        self.locked = False
        print("Unlocked the Car.")