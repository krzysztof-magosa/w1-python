import os
import glob
from w1.master import Master
from w1.therm import Therm
from w1 import consts as C
from w1 import families as Family

class Manager(object):
    def __init__(self):
        self.drivers = dict()
        self.register_driver(Family.THERM, Therm)

    def masters(self):
        for path in glob.iglob("{}/{}".format(C.DEVICES_PATH, "w1_bus_master*")):
            yield Master(
                manager=self,
                name=os.path.basename(path)
            )

    def register_driver(self, family, driver):
        self.drivers[str(family)] = driver

    def has_driver(self, family):
        return str(family) in self.drivers

    def get_driver(self, family):
        if self.has_driver(family):
            return self.drivers[family]
        else:
            return Slave

    def slaves(self, family=None, names=None):
        for master in self.masters():
            for slave in master.slaves(family=family, names=names):
                yield slave
