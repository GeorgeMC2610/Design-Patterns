from VGAcable import VGAcable
from USB2Cable import USB2Cable

class LowQualityCableFactory():

    def get_graphics_cable(self) -> VGAcable:
        return VGAcable()

    def get_usb_cable(self) -> USB2Cable:
        return USB2Cable()