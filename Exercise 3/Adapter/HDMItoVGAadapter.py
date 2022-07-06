from VGAinterface import VGAinterface
from HDMIcable import HDMIcable

class HDMItoVGAadapter(VGAinterface):

    def __init__(self, cable : HDMIcable):
        self.cable = cable

    def pins(self):
        return 15