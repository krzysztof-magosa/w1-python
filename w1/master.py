import os
from w1.device import Device
from w1 import consts as C

class Master(Device):
    def __init__(self, manager, name):
        self.manager = manager
        self.name = name
        self.path = "{}/{}".format(C.DEVICES_PATH, name)

    @property
    def slave_count(self):
        return int(self._read("w1_master_slave_count"))

    @property
    def slave_names(self):
        return self._read("w1_master_slaves").strip().split("\n")

    def slaves(self, family=None, names=None):
        for name in self.slave_names:
            slave_family = name.split("-")[0]

            if family and str(family) != slave_family:
                continue

            if names and name not in names:
                continue

            yield self.manager.get_driver(slave_family)(
                master=self,
                name=name
            )

    @property
    def pullup(self):
        return self._read("w1_master_pullup").strip() == "0" # 0 means enabled

    @pullup.setter
    def pullup(self, value):
        self._write("w1_master_pullup", "0" if value else "1")
