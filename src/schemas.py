from datetime import datetime

from pydantic import BaseModel


class BaseAlchemySchema(BaseModel):
    id: int
    created_on: datetime
    updated_on: datetime


class CreateBook(BaseModel):
    title: str
    pages_count: int


class CreateReview(BaseModel):
    content: str
    book_id: int


class ReviewDB(BaseAlchemySchema, CreateReview):
    class Config:
        orm_mode = True


class BookDB(BaseAlchemySchema, CreateBook):
    reviews: list[ReviewDB]

    class Config:
        orm_mode = True
