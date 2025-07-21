import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from crud_op.data_schemas import Base, Buyers, Battery_Sales

print("Starting to initialize database......")

DB_NAME = 'record_sales.db'



class Start_DB:
    def __init__(self):
        self.session = None
        self.engine = None

    def init_db(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        database = DB_NAME
        self.engine = create_engine(f'sqlite:///data/{database}')
        Base.metadata.create_all(self.engine)
    
    def get_db_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
        
db_object = Start_DB()
db_object.init_db()

def load_mock_data():
    buyers = [
        Buyers(name="John Doe", mobile="1234567890"),
        Buyers(name="Jane Smith", mobile="0987654321"),
        Buyers(name="Alice Johnson", mobile="5551234567"),
    ]

    battery_sales = [
        Battery_Sales(name="John Doe", mobile="1234567890", order_id=1, price=100.0),
        Battery_Sales(name="Jane Smith", mobile="0987654321", order_id=2, price=150.0),
        Battery_Sales(name="Alice Johnson", mobile="5551234567", order_id=3, price=200.0),
        Battery_Sales(name="Bob Brown", mobile="4445556666", order_id=4, price=250.0),
    ]

    session = db_object.get_db_session()
    session.add_all(buyers + battery_sales)
    session.commit()
    print("loaded mock data into database")
    
# load_mock_data()