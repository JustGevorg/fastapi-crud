from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime,
    func,
)


class BaseAlchemyModel(Base):
    """Base model with common fields for all entities"""

    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_on = Column(DateTime, default=func.now())
    updated_on = Column(DateTime, default=func.now(), onupdate=func.now())


class Book(BaseAlchemyModel):
    __tablename__ = "book"

    title = Column(
        String(length=125), index=True, unique=True, default="amazing description"
    )
    pages_count = Column(Integer)

    reviews = relationship("Review", back_populates="book")


class Review(BaseAlchemyModel):
    __tablename__ = "review"

    content = Column(Text)
    book_id = Column(Integer, ForeignKey("book.id"))
    approved = Column(Boolean, default=False)

    book = relationship("Book", back_populates="reviews")


class Community(BaseAlchemyModel):
    __tablename__ = "community"

    title = Column(String, index=True, unique=True)
