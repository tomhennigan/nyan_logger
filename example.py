import logging
from nyan_logger import NyanFormatter

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(NyanFormatter())
logger.addHandler(handler)

for _ in xrange(18 * 20):
    logger.info('nyan')