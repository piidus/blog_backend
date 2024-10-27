# logger_setup.py
import logging
from logging.handlers import RotatingFileHandler
import os
from .config import LOG_FILENAME

class IgnoreFlaskInternalLogs(logging.Filter):
    def filter(self, record):
        # Ignore logs from '_internal.py'
        return '_internal.py' not in record.pathname

def setup_logger():
    log_file_path = LOG_FILENAME
    if not os.path.exists(os.path.dirname(log_file_path)):
        os.makedirs(os.path.dirname(log_file_path))

    # Set up a rotating file handler
    file_handler = RotatingFileHandler(log_file_path, maxBytes=20000, backupCount=5)
    file_handler.setLevel(logging.DEBUG)

    # Set formatter to include filename and function name
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s'
    )
    file_handler.setFormatter(formatter)

    # Apply the filter to ignore Flask internal logs
    file_handler.addFilter(IgnoreFlaskInternalLogs())

    # Configure the root logger
    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    return logger



# import logging
# from logging.handlers import RotatingFileHandler
# import os
# def setup_logger(app):
#     # Ensure the log file path is valid
#     log_file_path = app.config['LOG_FILENAME']
#     if not os.path.exists(os.path.dirname(log_file_path)):
#         os.makedirs(os.path.dirname(log_file_path))

#     # Set up a rotating file handler
#     file_handler = RotatingFileHandler(log_file_path, maxBytes=20000, backupCount=5)
#     file_handler.setLevel(logging.DEBUG)
#     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
#     file_handler.setFormatter(formatter)
    
#     # Attach the handler to the app logger
#     app.logger.addHandler(file_handler)
#     app.logger.setLevel(logging.DEBUG)
#     app.logger.info("Logger has been set up and is writing to %s", log_file_path)
