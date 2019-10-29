import datetime
import logging

date = datetime.datetime.now()
logging.basicConfig(filename="update_log.ini", level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Updated at: %s" % date.now().strftime("%y%m%d_%H%M%S"))
