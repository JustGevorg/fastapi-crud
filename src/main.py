from fastapi import FastAPI
from src.routes import book_routes, review_routes

app = FastAPI()
app.include_router(book_routes.router)
app.include_router(review_routes.router)


@app.get("/")
async def index():
    return "Welcome to book club crud application!"
