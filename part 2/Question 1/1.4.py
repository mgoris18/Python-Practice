import logging
import sys

logging.basicConfig(level = logging.ERROR, format = ("%(levelname)s:%(message)s"), stream = sys.stdout)

def writeToFile(filename, text):
    try:
        with open (filename, 'w', encoding="utf-8") as f:
            content = f.write(text)
            print("Write successful")
    except Exception as e:
        logging.error(f"The exception that occurred is: {str(e)}")
