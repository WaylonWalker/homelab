import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

# log to ./log.log
logger.addHandler(logging.FileHandler("./log.log"))

for node in range(120):
    print(f"running {node+1} of 120")
    time.sleep(5)
    logger.info(f"done {node}")
