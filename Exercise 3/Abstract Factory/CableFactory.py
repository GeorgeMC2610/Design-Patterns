from GraphicsCable import GraphicsCable
from USBcable import USBcable

class CableFactory:

    def get_graphics_cable(self) -> GraphicsCable:
        pass

    def get_usb_cable(self) -> USBcable:
        pass