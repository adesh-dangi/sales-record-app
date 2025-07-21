from crud_op.setup_db import Start_DB
session = Start_DB().get_db_session()

from crud_op.data_schemas import Buyers, Battery_Sales, func

def add_buyer(name, mobile):
    new_buyer = Buyers(name=name, mobile=mobile)
    session.add(new_buyer)
    session.commit()
    print(f"Added buyer: {name}")

def add_battery_sale(name, mobile, order_id, price):
    new_sale = Battery_Sales(name=name, mobile=mobile, order_id=order_id, price=price)
    session.add(new_sale)
    session.commit()
    print(f"Added battery sale: {name}, Order ID: {order_id}, Price: {price}")

def get_all_buyers():
    buyers = session.query(Buyers).all()
    return buyers

def get_all_battery_sales_count_active_only():
    count = session.query(Battery_Sales).filter(Battery_Sales.active_sale == True).count()
    return count

def get_battery_sales_paginated(page=1, per_page=10):
    offset = (page - 1) * per_page
    sales = session.query(Battery_Sales).filter(Battery_Sales.active_sale == True).offset(offset).limit(per_page).all()
    return sales

def get_battery_sales_by_name(name):
    sales = session.query(Battery_Sales).filter(Battery_Sales.name == name, Battery_Sales.active_sale == True).all()
    return sales

def get_battery_sales_by_order_id(order_id):
    sales = session.query(Battery_Sales).filter(Battery_Sales.order_id == order_id, Battery_Sales.active_sale == True).all()
    return sales

def get_battery_sales_by_mobile(mobile):
    sales = session.query(Battery_Sales).filter(Battery_Sales.mobile == mobile, Battery_Sales.active_sale == True).all()
    return sales

def get_battery_sales_by_created_date_range(start_date, end_date):
    sales = session.query(Battery_Sales).filter(
        Battery_Sales.created_at >= start_date,
        Battery_Sales.created_at <= end_date,
        Battery_Sales.active_sale == True
    ).all()
    return sales

def soft_delete_sales_record(record_id):
    sale = session.query(Battery_Sales).filter(Battery_Sales.id == record_id, Battery_Sales.active_sale == True).first()
    if sale:
        session.query(Battery_Sales).filter(Battery_Sales.id == record_id).update({"active_sale": False, "updated_at": func.now})
        session.commit()
        print(f"Deleted sale record with ID: {record_id}")
    else:
        print(f"No sale record found with ID: {record_id}")