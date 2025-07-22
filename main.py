import os, sys
from crud_op import setup_db
from logs import c_logger as logger
from start_window import run_app

def check_dir_presence():
    if not os.path.exists('data'):
        os.makedirs('data')
        logger.info("Data directory created")
    if not os.path.exists('logs_files'):
        os.makedirs('logs')
        logger.info("Logs directory created")

if __name__ == "__main__":
    logger.info("Starting the application...from main.py")
    check_dir_presence()
    run_app()
    logger.info("App closed1")
    print("App closed2")