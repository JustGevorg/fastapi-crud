from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src import schemas, dependencies, services

router = APIRouter(prefix="/books")


@router.post("/", response_model=None)
async def create_book(
    new_book: schemas.CreateBook, db: Session = Depends(dependencies.get_db)
):
    service = services.BookService(db=db)
    created_book = service.create_book(new_book=new_book)
    return created_book
