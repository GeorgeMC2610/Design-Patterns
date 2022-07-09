from CableFactory import CableFactory
from GraphicsCable import GraphicsCable
from USBcable import USBcable
from DisplayPort import DisplayPort
from USBtypeC import USBtypeC

class HighQualityCable(CableFactory):

    def get_graphics_cable(self) -> GraphicsCable:
        return DisplayPort()

    def get_usb_cable(self) -> USBcable:
        return USBtypeC()