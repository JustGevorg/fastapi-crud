from fastapi import FastAPI
from src.routers import books_router

app = FastAPI()
app.include_router(books_router.router)


@app.get("/")
def index():
    return "Welcome to book club crud application!"
