from datetime import datetime
from pydantic import BaseModel


class BaseAlchemySchema(BaseModel):
    id: int
    created_on: datetime
    updated_on: datetime


class CreateBook(BaseModel):
    title: str
    pages_count: int


class BookDB(BaseAlchemySchema, CreateBook):
    class Config:
        orm_mode = True


class CreateReview(BaseModel):
    content: str
    book_id: int
