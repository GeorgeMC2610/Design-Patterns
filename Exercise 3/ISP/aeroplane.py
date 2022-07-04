from IMovable import IMovable
from ILockable import ILockable
from IFlying import IFlying

class Aeroplane(IMovable, ILockable, IFlying):

    def __init__(self) -> None:
        self.locked = False
        self.x = 0
        self.y = 0
        self.z = 0

    def move(self, x, y):

        if self.locked:
            print("Aeroplane is locked it cannot move!")
            return

        self.x += x
        self.y += y

        print(f"Successfully moved Aeroplane in position {self.x}, {self.y}.")

    def fly(self, x, y, z):

        if self.locked:
            print("Aeroplane is locked it cannot move!")
            return

        self.x += x
        self.y += y
        self.z += z

        print(f"Successfully flew Aeroplane in position {self.x}, {self.y}, {self.z}.")

    def lock(self):
        self.locked = True
        print("Locked the Aeroplane.")

    def unlock(self):
        self.locked = False
        print("Unlocked the Aeroplane.")