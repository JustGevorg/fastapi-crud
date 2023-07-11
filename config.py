from dotenv import load_dotenv
import os

load_dotenv()

# dev
DB_USER = os.environ.get("DB_USER")
DB_USER_PASSWORD = os.environ.get("DB_USER_PASSWORD")
DB_SERVER = os.environ.get("DB_SERVER")
DB_NAME = os.environ.get("DB_NAME")

# tests
TEST_DB_USER = os.environ.get("TEST_DB_USER")
TEST_DB_USER_PASSWORD = os.environ.get("TEST_DB_USER_PASSWORD")
TEST_DB_SERVER = os.environ.get("TEST_DB_SERVER")
TEST_DB_NAME = os.environ.get("TEST_DB_NAME")
