nyan_logger
===========

Nyan cat `logging.Formatter` implementation - https://pypi.python.org/pypi/nyan_logger

## Install

```
pip install nyan_logger
```

## Example

```python
import logging
from nyan_logger import NyanFormatter

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(NyanFormatter())
logger.addHandler(handler)

for _ in xrange(90):
    logger.info('nyan')
```

![img](http://f.cl.ly/items/2g2K0c3A2R1i2D051J3v/Screen%20Shot%202013-06-29%20at%2018.14.37.png)
