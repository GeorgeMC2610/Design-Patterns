from CableFactory import CableFactory
from GraphicsCable import GraphicsCable
from USBcable import USBcable
from VGAcable import VGAcable

class LowQualityCable(CableFactory):

    def get_graphics_cable(self) -> GraphicsCable:
        return VGAcable()

    def get_usb_cable(self) -> USBcable:
        return 