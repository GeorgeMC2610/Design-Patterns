from VGAinterface import VGAinterface
from HDMIcable import HDMIcable

class VGAtoHDMIadapter(VGAinterface):

    def __init__(self, cable : HDMIcable):
        self.cable = cable

    def pins(self):
        return 15