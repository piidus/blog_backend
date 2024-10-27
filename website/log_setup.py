import logging
from logging.handlers import RotatingFileHandler
import os
def setup_logger(app):
    # Ensure the log file path is valid
    log_file_path = app.config['LOG_FILENAME']
    if not os.path.exists(os.path.dirname(log_file_path)):
        os.makedirs(os.path.dirname(log_file_path))

    # Set up a rotating file handler
    file_handler = RotatingFileHandler(log_file_path, maxBytes=20000, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Attach the handler to the app logger
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.DEBUG)
    app.logger.info("Logger has been set up and is writing to %s", log_file_path)
