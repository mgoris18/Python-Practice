import logging
import sys

logging.basicConfig(level= logging.ERROR, format = "%(levelname)s:%(message)s", stream =sys.stdout)

def convertToInt(value):
    try:
        x = int(value)
        print(x)
    except Exception as e:
        logging.error(f"The exception that occurred is: {str(e)}")
        