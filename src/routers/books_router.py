from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src import schemas, dependencies, services

router = APIRouter(prefix="/books")


@router.get("/{book_id}", response_model=schemas.BookDB)
async def get_book(book_id: int, db: Session = Depends(dependencies.get_db)):
    service = services.BookService(db=db)
    target_book = service.get_book(book_id=book_id)

    return target_book


@router.post("/", response_model=schemas.BookDB)
async def create_book(
    new_book: schemas.CreateBook, db: Session = Depends(dependencies.get_db)
):
    service = services.BookService(db=db)
    created_book = service.create_book(new_book=new_book)

    return created_book


@router.put("/{book_id}", response_model=schemas.BookDB)
async def update_book(book_id: int, update_data: schemas.CreateBook, db: Session = Depends(dependencies.get_db)):
    service = services.BookService(db=db)
    updated_book = service.update_book(book_id=book_id, update_data=update_data)
    print(updated_book)
    # TODO: разобраться с one, first и проч
    return updated_book[0]
