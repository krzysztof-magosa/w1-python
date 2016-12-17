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

### w1-api
Simple HTTP server providing sensors values in JSON format.
At the moment only thermal sensors are supported.
Sensors are queried in separate thread every 1 second.
The api endpoint is `/sensors`.

Default settings, listen on 0.0.0.0:8080:
```
km@raspberrypi:~$ w1-api
```

Custom port and IP:
```
km@raspberrypi:~$ w1-api --port 1234 --ip 127.0.0.1
```

Example output:
```
[
    {
        "celsius": 61.25,
        "fahrenheit": 142.3616,
        "family": "28",
        "kelvin": 334.4,
        "name": "28-00000675de87",
        "serial": "00000675de87"
    },
    {
        "celsius": 24.937,
        "fahrenheit": 77.0,
        "family": "28",
        "kelvin": 298.15,
        "name": "28-000006762567",
        "serial": "000006762567"
    }
]
```
