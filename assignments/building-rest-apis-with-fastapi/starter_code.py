from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book API")


class BookInput(BaseModel):
    title: str
    author: str
    published_year: int


class Book(BookInput):
    id: int


books: list[Book] = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien", published_year=1937),
    Book(id=2, title="Frankenstein", author="Mary Shelley", published_year=1818),
]

# Add GET, POST, PUT, and DELETE endpoints for the book collection.
