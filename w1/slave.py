import os
from w1.device import Device
from w1 import consts as C

class Slave(Device):
    def __init__(self, master, name):
        self.master = master
        self.name = name
        self.path = "{}/{}".format(C.DEVICES_PATH, name)

    @property
    def family(self):
        return os.path.basename(self.path).split("-")[0]

    @property
    def serial(self):
        return os.path.basename(self.path).split("-")[1]
