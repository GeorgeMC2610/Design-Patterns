from VGAtoHDMIadapter import VGAtoHDMIadapter

class PC:

    def __init__(self, adapter : VGAtoHDMIadapter):
        self.adapter = adapter
        

    def connect_to_monitor(self):

        if self.adapter.pins() == 15:
            print("Monitor connected.")
        
        else:
            print("Something went wrong.")
