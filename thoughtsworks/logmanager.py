import logging

print logging.__file__
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, filename='booking.log')
logger = logging.getLogger('booking')

logger.info("Success: the booking is accepted!")
