# Define your method here
import logging
import sys
logging.basicConfig(level=logging.DEBUG, format='%(message)s', stream=sys.stdout)

if __name__ == '__main__':
    # Type your code here.
    log_number = input()
    parts = log_number.split()
    code = parts[1]
    
    if code == "10":
        logging.debug("Debug test\n")
    elif code == "20":
        logging.info("Program successful!\n")
    elif code == "30":
        logging.warning("Warning, there could be errors\n")
    elif code == "40":
        logging.error("Program encountered an error!\n")
    elif code == "50":
        logging.critical("The program has stopped working!\n")
    elif code == "60":
        logging.critical("System reboot required")
        
    

