nyan_logger
===========

Nyan cat `logging.Formatter` implementation - https://pypi.python.org/pypi/nyan_logger

## Install

```
pip install nyan_logger
```

## Example

Print the lyrics to the nyan cat song:

```python
import logging
from nyan_logger import NyanFormatter

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()

formatter = NyanFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.setLevel(logging.INFO)
for _ in xrange(90):
    logger.info('nyan')
```

## Screenshot

![img](http://f.cl.ly/items/2g2K0c3A2R1i2D051J3v/Screen%20Shot%202013-06-29%20at%2018.14.37.png)
