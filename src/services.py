from src import schemas
from src.db.models import Book
from sqlalchemy.orm import Session


class BaseService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def update(self, model, **kwargs):
        for k, v in kwargs.items():
            if hasattr(model, k):
                setattr(model, k, v)
            else:
                raise AttributeError


class BookService(BaseService):
    def create_book(self, new_book: schemas.CreateBook) -> Book:
        new_book = Book(**new_book.dict())
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)

        return new_book

    def get_book(self, book_id: int) -> Book:
        return self.db.query(Book).filter(Book.id == book_id).first()

    def update_book(self, book_id: int, update_data: schemas.CreateBook) -> Book:
        # updated_book = self.db.query(Book).filter(Book.id == book_id).update(values=update_data.dict())
        # self.db.commit()
        # self.db.refresh(updated_book)
        # print(updated_book)
        print(Book.__table__)
        return updated_book