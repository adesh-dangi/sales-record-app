import os
from crud_op import setup_db
from logs import logger


if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = Start_App()  # SplashScreen()
    # sys.exit(app.exec_())
    if not os.path.exists('data'):
        os.makedirs('data')
        logger.info("Data directory created")
    if not os.path.exists('logs'):
        os.makedirs('logs')
        logger.info("Logs directory created")

    logger.info("App closed1")
    print("App closed2")