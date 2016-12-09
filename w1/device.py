import os

class Device(object):
    def _read(self, filename):
        with open(os.path.join(self.path, filename), "r") as handler:
            return handler.read()

    def _write(self, filename, value):
        with open(os.path.join(self.path, filename), "w") as handler:
            return handler.write(value)
