from IMovable import IMovable
from ILockable import ILockable

class Car(IMovable, ILockable):
    
    def __init__(self) -> None:
        self.locked = False
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x += x
        self.y += y

    def lock(self):
        self.locked = True