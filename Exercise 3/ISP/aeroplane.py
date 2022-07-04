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
        self.x += x
        self.y += y

    def fly(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False