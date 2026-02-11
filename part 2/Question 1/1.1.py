import logging
import sys

def readFile(filename):
    logging.basicConfig(level=logging.ERROR, format="%(levelname)s:%(message)s", stream = sys.stdout)
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    except Exception as e:
        logging.error(f"The exception that occurred is: {str(e)}")