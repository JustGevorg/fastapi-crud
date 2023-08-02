from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src import dependencies, schemas, services

router = APIRouter(prefix="/reviews")


@router.post("/", response_model=schemas.ReviewDB)
async def create_review(
    new_review: schemas.CreateReview, db: Session = Depends(dependencies.get_db)
):
    service = services.ReviewService(db=db)
    created_review = service.create_review(new_review=new_review)

    db.commit()
    return created_review
