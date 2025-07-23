import pytest
from crud_op.crud_operation import get_bs_by_filter_keys
from datetime import datetime

# You may need to adjust these values based on your test DB setup

def test_search_by_name():
    sales, total = get_bs_by_filter_keys(name="John Doe")
    assert isinstance(sales, list)
    assert total >= 0
    for sale in sales:
        assert sale.name == "John Doe"


def test_search_by_mobile():
    sales, total = get_bs_by_filter_keys(mobile="1234567890")
    assert isinstance(sales, list)
    assert total >= 0
    for sale in sales:
        assert sale.mobile == "1234567890"


def test_search_by_order_id():
    sales, total = get_bs_by_filter_keys(order_id=1)
    assert isinstance(sales, list)
    assert total >= 0
    for sale in sales:
        assert sale.order_id == 1


def test_search_by_date():
    # Use a date that exists in your test DB
    date_search = datetime.now().date()  # Adjust as needed
    sales, total = get_bs_by_filter_keys(date_search=date_search)
    assert isinstance(sales, list)
    assert total >= 0
    for sale in sales:
        assert sale.created_at.date() == date_search


def test_search_by_multiple_fields():
    sales, total = get_bs_by_filter_keys(name="John Doe", mobile="1234567890", order_id=1)
    assert isinstance(sales, list)
    assert total >= 0
    for sale in sales:
        assert sale.name == "John Doe"
        assert sale.mobile == "1234567890"
        assert sale.order_id == 1


def test_search_pagination():
    sales_page_1, total_1 = get_bs_by_filter_keys(page=1, per_page=2)
    sales_page_2, total_2 = get_bs_by_filter_keys(page=2, per_page=2)
    assert isinstance(sales_page_1, list)
    assert isinstance(sales_page_2, list)
    assert total_1 == total_2
    # Ensure no overlap between pages if enough data
    if len(sales_page_1) > 0 and len(sales_page_2) > 0:
        ids_1 = set(sale.id for sale in sales_page_1)
        ids_2 = set(sale.id for sale in sales_page_2)
        assert ids_1.isdisjoint(ids_2)
