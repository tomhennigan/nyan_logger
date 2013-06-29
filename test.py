import logging
from nyan_logger import NyanFormatter

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()

formatter = NyanFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)

for _ in xrange(64):
    logger.info('nyan')