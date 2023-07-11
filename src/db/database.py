from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import config


SQLALCHEMY_DATABASE_URL = f"postgresql://{config.DB_USER}:{config.DB_USER_PASSWORD}@{config.DB_SERVER}/{config.DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
