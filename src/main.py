from fastapi import FastAPI
from src.routers import books

app = FastAPI()
app.include_router(books.router)


@app.get("/")
def index():
    return "Welcome to book club crud application!"
