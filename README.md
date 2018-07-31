# intelup_python

A package that sends data to Intelup platform.

# Basic usage

```python
from intelup_python import Intelup

# initialize with device token
intelup = Intelup("WQBhRxGrU8dEhfRy1WAQhD")

# send a single item
intelup.sendOne("Temperature", 25)

# you can pass custom timestamp in unix timestamp format
intelup.sendOne("Temperature", 25, 1533051583)
# or just let us do it for you

# send multiple items
data = [{"name": "Temperature", "value": 25}, {
    "name": "Humidity", "value": 33}, {"name": "WindSpeed", "value": 3}]

intelup.sendAll(data)

# with custom timestamp
intelup.sendAll(data, 1533051583)
```
