from DisplayPort import DisplayPort
from USBtypeC import USBtypeC

class HighQualityCableFactory():

    def get_graphics_cable(self) -> DisplayPort:
        return DisplayPort()

    def get_usb_cable(self) -> USBtypeC:
        return USBtypeC()