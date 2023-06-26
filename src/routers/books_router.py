from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src import schemas, dependencies, services

router = APIRouter(prefix="/books")

# @router.get('/{book_id}', response_model=)
# async def get_book():


@router.post("/", response_model=schemas.BookDB)
async def create_book(
    new_book: schemas.CreateBook, db: Session = Depends(dependencies.get_db)
):
    service = services.BookService(db=db)
    created_book = service.create_book(new_book=new_book)
    # Validation error for response model?
    return created_book
