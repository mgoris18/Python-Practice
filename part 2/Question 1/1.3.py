import logging
import sys

logging.basicConfig(level = logging.ERROR, format = ("%(levelname)s:%(message)s"), stream = sys.stdout)

def getListItem(lst, index):
    try: 
        print(lst[index])
    except Exception as e:
        logging.error(f"The exception that occurred is: {str(e)}")

