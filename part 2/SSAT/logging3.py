import logging
import sys

logging.basicConfig(level=logging.DEBUG, format='%(message)s', stream= sys.stdout)

if __name__ == '__main__':
    logging_number = input()
    event = logging_number.split()
    code = event[1]
    
    if code == "10":
        logging.debug("Initialization complete")
    elif code == "20":
        logging.info("User logged in successfully")
    elif code == "30":
        logging.warning("High memory usage detected")
    elif code == "40":
        logging.error("Unable to connect to server")
    elif code == "50":
        logging.critical("System shutdown initiated")

