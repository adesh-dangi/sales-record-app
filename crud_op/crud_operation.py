from crud_op.setup_db import Start_DB
session = Start_DB().get_db_session()

from datetime import datetime, timedelta
import calendar
from crud_op.data_schemas import Buyers, Battery_Sales, Product
from logs import c_logger as logger

def save_new_product_item(product_name):
    new_product= Product(name=product_name)
    session.add(new_product)
    session.commit()
    # logger.info(f"Added product: {new_product}")

def get_products_list():
    buyers = session.query(Product).filter(Product.active==True).all()
    return buyers

def add_buyer(name, mobile):
    new_buyer = Buyers(name=name, mobile=mobile)
    session.add(new_buyer)
    session.commit()
    # logger.info(f"Added buyer: {name}")

def add_battery_sale(name, mobile, order_id, price, product):
    new_sale = Battery_Sales(name=name, mobile=mobile, order_id=order_id, price=price, product=product,created_at=datetime.now(), updated_at=datetime.now())
    session.add(new_sale)
    session.commit()
    # logger.info(f"Added battery sale: {name}, Order ID: {order_id}, Price: {price}")

def get_all_buyers():
    buyers = session.query(Buyers).all()
    return buyers

def get_all_battery_sales_count_active_only():
    count = session.query(Battery_Sales).filter(Battery_Sales.active_sale == True).count()
    return count

def get_battery_sales_paginated(page=1, per_page=10):
    offset = (page - 1) * per_page
    sales = session.query(Battery_Sales).filter(Battery_Sales.active_sale == True).order_by(Battery_Sales.created_at.desc()).offset(offset).limit(per_page).all()
    return sales

def get_battery_sales_by_id(id):
    sale = session.query(Battery_Sales).filter(Battery_Sales.id == id).first()
    return sale

def get_bs_by_filter_keys(name="", mobile="", order_id="", date_search_month="", date_search_year="", page=1, per_page=10):
    offset = (page - 1) * per_page
    search_query = [Battery_Sales.active_sale == True]
    if name:
        search_query.append(Battery_Sales.name.ilike(f"%{name}%"))
    if mobile:
        search_query.append(Battery_Sales.mobile == mobile)
    if order_id:
        search_query.append(Battery_Sales.order_id == order_id)
    if date_search_month and date_search_year:
        # Convert month name to month number
        month_number = datetime.strptime(date_search_month, "%B").month
        year_number = int(date_search_year)

        # Start date: first day of month
        start_date = datetime(year_number, month_number, 1)

        # End date: last day of month + 1 day - 1 microsecond
        last_day = calendar.monthrange(year_number, month_number)[1]
        end_date = datetime(year_number, month_number, last_day, 23, 59, 59, 999999)

        # print("start:", start_date, "end:", end_date)

        # SQLAlchemy query
        search_query.append(
            Battery_Sales.created_at.between(start_date, end_date)
        )
    # print("search_query", *search_query)
    sales_data = session.query(Battery_Sales).filter(
        *search_query
    ).order_by(Battery_Sales.created_at.desc()).offset(offset).limit(per_page).all()
    total_count = session.query(Battery_Sales).filter(*search_query).count()
    return sales_data, total_count

def get_battery_sales_by_name(name):
    sales = session.query(Battery_Sales).filter(Battery_Sales.name == name, Battery_Sales.active_sale == True).order_by(Battery_Sales.created_at.desc()).all()
    return sales

def get_battery_sales_by_order_id(order_id):
    sales = session.query(Battery_Sales).filter(Battery_Sales.order_id == order_id, Battery_Sales.active_sale == True).order_by(Battery_Sales.created_at.desc()).all()
    return sales

def get_battery_sales_by_mobile(mobile):
    sales = session.query(Battery_Sales).filter(Battery_Sales.mobile == mobile, Battery_Sales.active_sale == True).order_by(Battery_Sales.created_at.desc()).all()
    return sales

def get_battery_sales_by_created_date_range(start_date, end_date):
    sales = session.query(Battery_Sales).filter(
        Battery_Sales.created_at >= start_date,
        Battery_Sales.created_at <= end_date,
        Battery_Sales.active_sale == True
    ).order_by(Battery_Sales.created_at.desc()).all()
    return sales

def soft_delete_sales_record(record_id):
    sale = session.query(Battery_Sales).filter(Battery_Sales.id == record_id, Battery_Sales.active_sale == True).first()
    if sale:
        session.query(Battery_Sales).filter(Battery_Sales.id == record_id).update({"active_sale": False, "updated_at": datetime.now()})
        session.commit()
        logger.info(f"Deleted sale record with ID: {record_id}")
    else:
        logger.info(f"No sale record found with ID: {record_id}")