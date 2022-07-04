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
        self.x += x
        self.y += y

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def hook_trailer(self):
        self.trailer = True

    def detach_trailer(self):
        self.trailer = False