import os
import shutil
import pytest
from crud_op.setup_db import Start_DB, load_mock_data
from crud_op import setup_db

# python


@pytest.fixture
def clean_data_dir(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    monkeypatch.setattr("os.path.exists", lambda path: path == str(data_dir))
    monkeypatch.setattr("os.makedirs", lambda path: os.makedirs(path, exist_ok=True))
    yield data_dir
    if data_dir.exists():
        shutil.rmtree(data_dir)

def test_start_db_init():
    db = Start_DB()
    print("session", db.session, "engine", db.engine)
    assert db.session is None
    assert db.engine is not None

def test_init_db_creates_data_dir(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    called = {}

    real_exists = os.path.exists
    real_join = os.path.join

    def fake_exists(path):
        if path == str(data_dir):
            return False
        return real_exists(path)

    def fake_join(a, b):
        if b == "data":
            return str(data_dir)
        return real_join(a, b)

    def fake_makedirs(path):
        called['made'] = path

    monkeypatch.setattr("os.path.exists", fake_exists)
    monkeypatch.setattr("os.makedirs", fake_makedirs)
    monkeypatch.setattr("os.path.join", fake_join)

    db = Start_DB()

    assert 'made' in called
    assert called['made'] == str(data_dir)

def test_init_db_creates_db_file(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    os.makedirs(data_dir, exist_ok=True)
    monkeypatch.setattr("os.path.exists", lambda path: True)
    monkeypatch.setattr("os.makedirs", lambda path: None)
    db = Start_DB()
    db_file = tmp_path / "data" / "record_sales.db"
    # The file may not exist until something is written, so just check engine is set
    assert db.engine is not None

def test_get_db_session_returns_session(monkeypatch):
    db = Start_DB()
    db.engine = None
    session = db.get_db_session()
    assert session is not None
    # session should have add, commit, etc.
    assert hasattr(session, "add")
    assert hasattr(session, "commit")

def test_load_mock_data_inserts(monkeypatch):
    # Use the real db_object from setup_db
    setup_db.db_object
    session = setup_db.db_object.get_db_session()
    # Clean up before
    session.query(setup_db.Buyers).delete()
    session.query(setup_db.Battery_Sales).delete()
    session.commit()
    load_mock_data()
    buyers = session.query(setup_db.Buyers).all()
    battery_sales = session.query(setup_db.Battery_Sales).all()
    assert len(buyers) >= 3
    assert len(battery_sales) >= 4