import logging
import time

class logger():

    def __init__(self, logger, file_level = logging.INFO):

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime("%Y-%m-%d")
        self.log_file_name = "..\\logs\\log"+curr_time+'.txt'
        file_handler = logging.FileHandler(self.log_file_name,mode='w')
        file_handler.setFormatter(fmt)
        file_handler.setLevel(file_level)
        self.logger.addHandler(file_handler)
