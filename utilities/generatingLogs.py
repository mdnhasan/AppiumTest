import logging

# logging.basicConfig(filename="..\\logs\\logfile.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'
#                     ,level=logging.INFO)
#
# log = logging.getLogger()
#
# log.info("This is our log")

def log():
    logging.basicConfig(filename="..\\logs\\logfile.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p'
                        , level=logging.INFO)

    logger = logging.getLogger()
    return logger

logger = log()
logger.info("This is New LOG")
logger.error("This is error")