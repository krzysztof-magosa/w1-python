# w1
Python wrapper for 1-wire Linux interface

## Prerequisites
`w1` library is just simple wrapper for `/sys/bus/w1` interface provided by Linux Kernel.
To use it you need to load module `wire`:
```
# modprobe wire
```

To have module `wire` loaded across reboots you may need to add it to system modules configuration, e.g. `/etc/modules` or similar (depending on Linux distribution).

## Usage
```python
from w1 import Manager
from w1 import Family

manager = Manager()
for slave in manager.slaves(family=Family.THERM):
    print(slave.temperature)
```

## Utilities
### w1-therm

`w1` library comes with handy `w1-therm` utility which is useful while writing shell scripts.

Show temperature from all thermometers:
```
km@raspberrypi:~$ w1-therm
28-00000675de87   58.69
28-000006762567   27.56
```

You can also see just selected thermometer(s):
```
km@raspberrypi:~$ w1-therm --name 28-000006762567
28-000006762567   27.56
```

If you want just to see value from one thermometer:
```
km@raspberrypi:~$ w1-therm --name 28-000006762567 --only-value
27.56
```

In scripts it may be useful to get just integer:
```
km@raspberrypi:~$ w1-therm --name 28-000006762567 --only-value --as-integer
28
```

And of course you can use different units:
```
km@raspberrypi:~$ w1-therm --name 28-000006762567 --only-value --as-integer --unit celsius
28
km@raspberrypi:~$ w1-therm --name 28-000006762567 --only-value --as-integer --unit kelvin
301
km@raspberrypi:~$ w1-therm --name 28-000006762567 --only-value --as-integer --unit fahrenheit
82
```
