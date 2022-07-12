from CableFactory import CableFactory
from GraphicsCable import GraphicsCable
from USBcable import USBcable
from HDMIcable import HDMIcable
from USB3Cable import USB3Cable

class MediumQualityCableFactory(CableFactory):

    def get_graphics_cable(self) -> GraphicsCable:
        return HDMIcable()

    def get_usb_cable(self) -> USBcable:
        return USB3Cable()