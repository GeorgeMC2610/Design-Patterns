#ADAPTER DESIGN PATTERN
#this example shows a proof of concept for a monitor connecting to a pc.
#the monitor is vga-type and the pc only has an hdmi port. So we created the VGA to HDMI adapter class to handle this.

from HDMIcable import HDMIcable
from VGAtoHDMIadapter import VGAtoHDMIadapter
from PC import PC

hdmi_cable = HDMIcable()
vga_to_hdmi_adapter = VGAtoHDMIadapter(hdmi_cable)
pc = PC(vga_to_hdmi_adapter)

pc.connect_to_monitor()