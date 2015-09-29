#!/usr/bin/env python
import logging
from nyan_logger import NyanFormatter

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(NyanFormatter(4))
logger.addHandler(handler)

try:
    for _ in range(18 * 2000):
        logger.info('nyan')
except KeyboardInterrupt:
    exit()
