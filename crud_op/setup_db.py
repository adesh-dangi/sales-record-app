import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from crud_op.data_schemas import Base, Buyers, Battery_Sales
from logs import c_logger
from datetime import datetime

c_logger.info("Starting to initialize database......")

DB_NAME = 'record_sales.db'


class Start_DB:
    def __init__(self):
        self.session = None
        self.engine = None
        self.session = None
        self.data_dir = os.path.join(os.getcwd(), "data")
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        database = DB_NAME
        self.engine = create_engine(f'sqlite:///data/{database}')
        Base.metadata.create_all(self.engine)
    
    def get_db_session(self):
        if self.session is not None:
            return self.session
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        return self.session

db_object = Start_DB()

def load_mock_data():
    session = db_object.get_db_session()
    buyers = [
        Buyers(name="John Doe", mobile="1234567890"),
        Buyers(name="Jane Smith", mobile="0987654321"),
        Buyers(name="Alice Johnson", mobile="5551234567"),
    ]
    session.add_all(buyers)

    battery_sales = [
        Battery_Sales(name="John Doe", mobile="1234567890", order_id=1, price=100.0, created_at=datetime.now(), updated_at=datetime.now()),
        Battery_Sales(name="Jane Smith", mobile="0987654321", order_id=2, price=150.0, created_at=datetime.now(), updated_at=datetime.now()),
        Battery_Sales(name="Alice Johnson", mobile="5551234567", order_id=3, price=200.0, created_at=datetime.now(), updated_at=datetime.now()),
        Battery_Sales(name="John Doe", mobile="1234567890", order_id=4, price=120.0, created_at=datetime.now(), updated_at=datetime.now()),
    ]
    session.add_all(battery_sales)

    # session.add_all(buyers + battery_sales) can be done in one short

    session.commit()
    c_logger.info("loaded mock data into database")
    
# load_mock_data()