from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src import dependencies, schemas, services

router = APIRouter(prefix="/books")


@router.get(
    "/{book_id}",
    response_model=schemas.BookDB,
    description="Get all book information except reviews list",
)
async def get_book(book_id: int, db: Session = Depends(dependencies.get_db)):
    service = services.BookService(db=db)
    target_book = service.get_book(book_id=book_id)

    db.commit()
    return target_book


# TODO: response_model causes an extra selects!!!
# TODO: need remove db.commit() from services and move into endopint layer for run multiple endpoint operations in SINGLE transaction  # noqa: E501
@router.post("/", response_model=schemas.BookDB)
async def create_book(
    new_book: schemas.CreateBook, db: Session = Depends(dependencies.get_db)
):
    service = services.BookService(db=db)
    created_book = service.create_book(new_book=new_book)

    service.commit_changes()
    return created_book


@router.put("/{book_id}", response_model=schemas.BookDB)
async def update_book(
    book_id: int,
    update_data: schemas.CreateBook,
    db: Session = Depends(dependencies.get_db),
):
    service = services.BookService(db=db)
    updated_book = service.update_book(book_id=book_id, update_data=update_data)

    service.commit_changes()
    return updated_book


@router.delete("/{book_id}", response_model=None)
async def delete_book(book_id: int, db: Session = Depends(dependencies.get_db)):
    service = services.BookService(db=db)
    deleted_book = service.delete_book(book_id=book_id)

    service.commit_changes()
    return deleted_book


@router.get("/{book_id}/reviews", response_model=schemas.BookDB)
async def get_book_with_related_reviews(
    book_id: int, db: Session = Depends(dependencies.get_db)
):
    service = services.BookService(db=db)
    book_and_related_reviews = service.get_book_and_related_reviews(book_id=book_id)

    service.commit_changes()
    return book_and_related_reviews
