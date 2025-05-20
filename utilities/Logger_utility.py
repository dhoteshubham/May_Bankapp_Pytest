import logging


class logger_class:
    @staticmethod
    def log_gen_method():
        log_file = logging.FileHandler(".\\Logs\\bankapp.log") #log file
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') #log format
        log_file.setFormatter(log_format) #log file --->format
        logger = logging.getLogger()
        logger.addHandler(log_file) #log addhandler ---> every time add the log
        logger.setLevel(logging.INFO) #set log level
        return logger



# log file
# log format
# log file --->format
# log addhandler ---> every time add the log
# set log level

