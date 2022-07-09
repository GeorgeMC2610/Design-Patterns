# FACTORY DESIGN PATTERN
# Assuming that we have several cables, that offer different speeds.
# USB 2.0 and VGA offer slower speeds
# USB 3.0 and HDMI offer faster speeds
# USB type-C and Display Port are the fastest available.
# but we offer several qualities from several factories.

from CableFactory import CableFactory
from LowQualityCableFactory import LowQualityCableFactory
from MediumQualityCableFactory import MediumQualityCableFactory
from HighQualityCableFactory import HighQualityCableFactory


def read_quality() -> CableFactory:

    qualities = {
        'low':    LowQualityCableFactory(),
        'medium': MediumQualityCableFactory(),
        'high':   HighQualityCableFactory()
    }

    quality = input("What cable quality would you like? (low, medium, high) --> ")

    if quality.lower() in qualities:
        return qualities[quality]
    
    print("That was wrong. Try again.")
    return read_quality()



factory = read_quality()

graphics_cable = factory.get_graphics_cable()
usb_cable = factory.get_usb_cable()

graphics_cable.show_graphics()
usb_cable.transfer()
