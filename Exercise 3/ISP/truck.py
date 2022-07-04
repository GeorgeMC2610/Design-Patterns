from IMovable import IMovable
from ILockable import ILockable
from ITrailerHooker import ITrailerHooker

class Truck(IMovable, ILockable, ITrailerHooker):

    def __init__(self) -> None:
        self.locked = False
        self.x = 0
        self.y = 0
        self.trailer = False

    def move(self, x, y):

        if self.locked:
            print("Truck is locked it cannot move!")
            return

        self.x += x
        self.y += y

        print(f"Successfully moved Truck in position {x}, {y}.")

    def lock(self):
        self.locked = True
        print("Locked the Truck.")

    def unlock(self):
        self.locked = False
        print("Unlocked the Truck.")

    def hook_trailer(self):
        self.trailer = True
        print("Truck was hooked on a trailer!.")

    def detach_trailer(self):
        self.trailer = False
        print("Detached trailer from the Truck.")