import logging
import sys

logging.basicConfig(level = logging.DEBUG, format= "%(levelname)s: %(message)s", stream = sys.stdout)

x = int(input())
y = int(input())

try:
    print(x/y)
except ZeroDivisionError as e:
    logging.error(f"The exception that occured is: {e}")