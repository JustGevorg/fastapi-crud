from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session

from src import schemas
from src.db.models import Book, Review


class BaseService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def commit_changes(self) -> None:
        """Commit query changes and and finish transaction"""
        self.db.commit()


class BookService(BaseService):
    def create_book(self, new_book: schemas.CreateBook) -> Book:
        stmt = insert(Book).values(new_book.dict()).returning(Book)
        new_book = self.db.execute(stmt).scalars().first()

        return new_book

    def get_book(self, book_id: int) -> Book:
        return self.db.query(Book).filter(Book.id == book_id).first()

    def update_book(self, book_id: int, update_data: schemas.CreateBook) -> Book:
        stmt = (
            update(Book)
            .where(Book.id == book_id)
            .values(update_data.dict())
            .returning(Book)
        )
        updated_book = (self.db.execute(stmt)).scalars().first()
        self.db.commit()

        return updated_book

    def delete_book(self, book_id: int) -> None:
        stmt = (
            delete(Book)
            .where(Book.id == book_id)
            .returning(Book.title, Book.pages_count)
        )
        deleted_book = (self.db.execute(stmt)).scalars().all()
        self.db.commit()

        return deleted_book

    def get_book_and_related_reviews(self, book_id: int) -> Book:
        stmt = select(Book).join(Book.reviews)
        book_with_related_reviews = (self.db.execute(stmt)).scalar()
        self.db.commit()

        return book_with_related_reviews


class ReviewService(BaseService):
    def create_review(self, new_review: schemas.CreateReview) -> Review:
        stmt = insert(Review).values(new_review.dict()).returning(Review)
        created_review = self.db.execute(stmt)

        return created_review.scalars().first()
