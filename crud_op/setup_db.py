import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from crud_op.data_schemas import Base, Buyers, Battery_Sales
from logs import c_logger as logger
from datetime import datetime

logger.info("Starting to initialize database......")

DB_NAME = 'record_sales.db'

test_env = os.getenv("TEST_ENV")
# export TEST_ENV=py_test_active
class Start_DB:
    def __init__(self):
        self.session = None
        self.engine = None
        self.session = None
        self.data_dir = os.path.join(os.getcwd(), "data")
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        database = DB_NAME
        if test_env=="py_test_active":
            self.engine = create_engine(f'sqlite:///data/{database}')
        else:
            self.engine = create_engine(f'sqlite:///{os.path.abspath(os.path.join(self.data_dir, database))}')
        Base.metadata.create_all(self.engine)
    
    def get_db_session(self):
        if self.session is not None:
            return self.session
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        return self.session


def gen_random_str(lenght=5):
    import random, string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(lenght))

def gen_random_mobile_num(lenght=10):
    import random, string
    return ''.join(random.choice(string.digits) for _ in range(lenght))

def load_mock_data():
    session = db_object.get_db_session()
    buyers = [
        Buyers(name="John Doe", mobile="1234567890"),
        Buyers(name="Jane Smith", mobile="0987654321"),
        Buyers(name="Alice Johnson", mobile="5551234567"),
    ]
    session.add_all(buyers)

    battery_sales = [
        Battery_Sales(name="John Doe", mobile="1234567890", order_id='T1jygkyjghjku12320', price=100.0, created_at=datetime.now(), updated_at=datetime.now(),product="battery"),
        Battery_Sales(name="Jane Smith", mobile="0987654321", order_id="T1jygkyjghjku12322", price=150.0, created_at=datetime.now(), updated_at=datetime.now(),product="battery"),
        Battery_Sales(name="Alice Johnson", mobile="5551234567", order_id="T1jygkyjghjku12321", price=200.0, created_at=datetime.now(), updated_at=datetime.now(),product="battery"),
        Battery_Sales(name="John Doe", mobile="1234567890", order_id="T1jygkyjghjku1232", price=120.0, created_at=datetime.now(), updated_at=datetime.now(),product="battery"),
        Battery_Sales(name=f"John {gen_random_str(5)}", mobile=gen_random_mobile_num(), order_id=gen_random_str(lenght=15), price=10000.0, created_at=datetime.now(), updated_at=datetime.now(),product="battery"),
        Battery_Sales(name=f"Jane {gen_random_str(5)}", mobile=gen_random_mobile_num(), order_id=gen_random_str(lenght=15), price=1500.0, created_at=datetime.now(), updated_at=datetime.now(),product="battery"),
        Battery_Sales(name=f"Alice {gen_random_str(5)}", mobile=gen_random_mobile_num(), order_id=gen_random_str(lenght=15), price=20000.0, created_at=datetime.now(), updated_at=datetime.now(),product="battery"),
        Battery_Sales(name=f"John {gen_random_str(5)}", mobile=gen_random_mobile_num(), order_id=gen_random_str(lenght=15), price=120000.0, created_at=datetime.now(), updated_at=datetime.now(),product="battery"),
    ]
    session.add_all(battery_sales)

    # session.add_all(buyers + battery_sales) can be done in one short

    session.commit()
    session.close()
    logger.info("loaded mock data into database")
    
db_object = Start_DB()

if test_env=="py_test_active":
    load_mock_data()


# for i in range(5):
#     load_mock_data()

