import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger()

class LogLevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno <= self.level

formatter = logging.Formatter('%(levelname)s - %(message)s')

debug_info = logging.FileHandler('debug_info.log', encoding="utf-8", mode='w')
debug_info.addFilter(LogLevelFilter(logging.INFO))
# debug_info.setLevel(logging.DEBUG)
debug_info.setFormatter(formatter)
logger.addHandler(debug_info)

warnings_info = logging.FileHandler('warnings_errors.log', encoding="utf-8", mode='w')
warnings_info.setLevel(logging.WARNING)
warnings_info.setFormatter(formatter)
logger.addHandler(warnings_info)

logger.debug('Это DEBUG')
logger.info('Это INFO')
logger.warning('Это WARNING')
logger.error('Это ERROR')
logger.critical('Это CRITICAL')