from src import schemas
from src.db.models import Book, Review
from src.services import BookService, ReviewService
from src.tests.conftest import override_get_db


# not sure if this is the best way to test services
def test_create_book_service():
    service = BookService(db=next(override_get_db()))
    created_book = service.create_book(
        schemas.CreateBook(title="spam_created", pages_count=10212)
    )
    assert isinstance(created_book, Book)


def test_review_service():
    service = ReviewService(db=next(override_get_db()))
    created_review = service.create_review(
        new_review=schemas.CreateReview(content="test foo content", book_id=8)
    )

    assert isinstance(created_review, Review)
