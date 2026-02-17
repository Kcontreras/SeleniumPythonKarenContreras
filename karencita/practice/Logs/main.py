import logging

def log_details():
    logging.basicConfig(
        filename="demo_test.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %p"
    )
    return logging.getLogger()

logger = log_details()  
logger.info("Program execution started")

a = 10
b = 3

if a>b:
    print("Karen")
    logger.info("A is greater than B")
logger.info("Program execution completed")
