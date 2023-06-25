from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from .. import dependencies
from .. import services

router = APIRouter(prefix="/books")


@router.post("/", response_model=None)
async def create_book(
    new_book: schemas.CreateBook, db: Session = Depends(dependencies.get_db)
):
    service = services.BookService(db=db)
    print(new_book.dict())
    created_book = service.create_book(new_book=new_book)
    # return created_book
    return "Hello"
