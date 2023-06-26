from src import schemas
from src.db.models import Book
from sqlalchemy.orm import Session


class BaseService:
    def __init__(self, db: Session) -> None:
        self.db = db


class BookService(BaseService):
    def create_book(self, new_book: schemas.CreateBook):
        new_book = Book(**new_book.dict())
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        return new_book
