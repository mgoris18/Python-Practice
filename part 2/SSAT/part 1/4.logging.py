import logging
import sys

logging.basicConfig(level= logging.ERROR, format = "%(levelname)s: %(message)s", stream= sys.stdout)

x = input()
try:
    y = (int(x))
    print(y * 10)
except ValueError as e:
    logging.error(f"Invalid input: {e}")

