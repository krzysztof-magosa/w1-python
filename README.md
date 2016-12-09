# w1
Python wrapper for 1-wire Linux interface

## Usage
```python
from w1 import Manager
from w1 import Family

manager = Manager()
for slave in manager.slaves(family=Family.THERMAL):
    print(slave.temperature)
```
