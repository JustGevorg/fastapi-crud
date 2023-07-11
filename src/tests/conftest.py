from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.database import Base
from src.db.models import Book
from src.dependencies import get_db
from src.main import app
import config
import pytest


TEST_SQLALCHEMY_DATABASE_URL = f"postgresql://{config.TEST_DB_USER}:{config.TEST_DB_USER_PASSWORD}@{config.TEST_DB_SERVER}/{config.TEST_DB_NAME}"

test_engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=test_engine)


def pytest_sessionfinish(session, exitstatus):
    TestingSessionLocal().close_all()
    Base.metadata.drop_all(bind=test_engine)


app.dependency_overrides[get_db] = override_get_db

test_client = TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def create_fake_books():
    ss = next(override_get_db())
    for i in range(10):
        new_book = Book(title=f"title{i}", pages_count=100 + i)
        ss.add(new_book)
        ss.commit()
