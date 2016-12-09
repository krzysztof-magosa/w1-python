import os
import re
import glob
from w1.slave import Slave

class Therm(Slave):
    @property
    def temperature(self):
        data = self._read("w1_slave")

        match = re.search("crc=(\w+) (\w+)", data)
        if match.group(2) != "YES":
            raise RuntimeError("CRC error during transmission.")

        match = re.search("t=(\d+)", data)
        return int(match.group(1)) / 1000.0
