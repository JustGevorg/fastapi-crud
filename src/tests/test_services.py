from src.services import BookService
from src.db.models import Book

from src import schemas
from src.tests.conftest import override_get_db


# not sure if this is the best way to test services
def test_create_book_service():
    service = BookService(db=next(override_get_db()))
    created_book = service.create_book(
        schemas.CreateBook(title="spam_created", pages_count=10212)
    )
    assert isinstance(created_book, Book)
