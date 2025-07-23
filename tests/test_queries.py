import pytest
from crud_op.setup_db import load_mock_data, db_object
from crud_op import crud_operation, setup_db
from datetime import datetime, timedelta

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    session = db_object.get_db_session()
    # Clean up before loading mock data
    session.query(setup_db.Buyers).delete()
    session.query(setup_db.Battery_Sales).delete()
    session.commit()
    load_mock_data()
    yield
    # Clean up after tests
    session.query(setup_db.Buyers).delete()
    session.query(setup_db.Battery_Sales).delete()
    session.commit()

def test_get_all_buyers():
    buyers = crud_operation.get_all_buyers()
    assert len(buyers) >= 3
    assert any(b.name == "John Doe" for b in buyers)

def test_get_all_battery_sales_count_active_only():
    count = crud_operation.get_all_battery_sales_count_active_only()
    assert count >= 4

def test_get_battery_sales_paginated():
    sales = crud_operation.get_battery_sales_paginated(page=1, per_page=2)
    assert len(sales) == 2

def test_get_battery_sales_by_name_found():
    sales = crud_operation.get_battery_sales_by_name("Jane Smith")
    assert sales
    assert all(s.name == "Jane Smith" for s in sales)

def test_get_battery_sales_by_name_not_found():
    sales = crud_operation.get_battery_sales_by_name("Ghost Buyer")
    assert sales == []

def test_get_battery_sales_by_order_id_found():
    sales = crud_operation.get_battery_sales_by_order_id("T1jygkyjghjku12321")
    assert sales
    assert all(s.order_id == "T1jygkyjghjku12321" for s in sales)

def test_get_battery_sales_by_order_id_not_found():
    sales = crud_operation.get_battery_sales_by_order_id(999)
    assert sales == []

def test_get_battery_sales_by_mobile_found():
    sales = crud_operation.get_battery_sales_by_mobile("1234567890")
    assert sales
    assert all(s.mobile == "1234567890" for s in sales)

def test_get_battery_sales_by_mobile_not_found():
    sales = crud_operation.get_battery_sales_by_mobile("0000000000")
    assert sales == []

def test_get_battery_sales_by_created_date_range():
    # Use a wide range to include all mock data
    start = datetime.now() - timedelta(days=365)
    end = datetime.now() + timedelta(days=1)
    sales = crud_operation.get_battery_sales_by_created_date_range(start, end)
    assert sales
    assert all(s.created_at >= start and s.created_at <= end for s in sales)

def test_soft_delete_sales_record():
    # Get a sale to delete
    sales = crud_operation.get_battery_sales_by_name("John Doe")
    if not sales:
        pytest.skip("No sales to delete")
    sale_id = sales[0].id
    print(sale_id)
    crud_operation.soft_delete_sales_record(sale_id)
    # # Should not be returned in active sales now
    active_sales = crud_operation.get_battery_sales_by_name("John Doe")
    assert all(s.id != sale_id for s in active_sales)