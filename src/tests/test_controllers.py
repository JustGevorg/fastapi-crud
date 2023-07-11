from conftest import test_client

from src import schemas
import pytest
import pydantic


def test_index_controller():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to book club crud application!"


def test_create_book_controller():
    response = test_client.post(
        url="/books/", json={"title": "foobafdfdfr", "pages_count": 120}
    )
    assert schemas.BookDB(**response.json())


def test_get_book_controller():
    response = test_client.get(url="/books/1")
    assert schemas.BookDB(**response.json())


def test_update_book_controller():
    book_with_old_title = test_client.get(url="/books/3")
    old_book_title = schemas.BookDB(**book_with_old_title.json()).title

    new_book_title = "awesome_title"

    book_with_updated_title = test_client.put(
        url="/books/1", json={"title": new_book_title, "pages_count": 120}
    )
    updated_book_title = schemas.BookDB(**book_with_updated_title.json()).title

    assert old_book_title != new_book_title and updated_book_title == new_book_title


def test_delete_book_controller():
    deleted_book = test_client.delete(url="/books/3")
    print(deleted_book)
    with pytest.raises(pydantic.ValidationError):
        test_client.get(url="/books/3")
