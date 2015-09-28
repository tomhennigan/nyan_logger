#!/usr/bin/env python
import logging
from nyan_logger import NyanFormatter

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(NyanFormatter())
logger.addHandler(handler)

for _ in range(18 * 20):
    logger.info('nyan')