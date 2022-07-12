from HDMIcable import HDMIcable
from USB3Cable import USB3Cable

class MediumQualityCableFactory():

    def get_graphics_cable(self) -> HDMIcable:
        return HDMIcable()

    def get_usb_cable(self) -> USB3Cable:
        return USB3Cable()