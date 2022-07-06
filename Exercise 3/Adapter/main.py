#ADAPTER DESIGN PATTERN
#this example shows a proof of concept for a monitor connecting to a pc.
#the monitor is hdmi and the pc only has a vga port. So we created the HDMI to VGA adapter class to handle this.

from HDMIcable import HDMIcable
from HDMItoVGAadapter import HDMItoVGAadapter
from PC import PC

hdmi_cable = HDMIcable()
vga_to_hdmi_adapter = HDMItoVGAadapter(hdmi_cable)
pc = PC(vga_to_hdmi_adapter)

pc.connect_to_monitor()