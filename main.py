import os
from crud_op import setup_db



if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # window = Start_App()  # SplashScreen()
    # sys.exit(app.exec_())
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('logs'):
        os.makedirs('data')
    print("app closed")