from fastapi import FastAPI, HTTPException, Response, status
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
_next_book_id = 3


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput) -> Book:
    global _next_book_id
    book = Book(id=_next_book_id, **book_input.model_dump())
    _next_book_id += 1
    books.append(book)
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput) -> Book:
    for index, book in enumerate(books):
        if book.id == book_id:
            updated_book = Book(id=book_id, **book_input.model_dump())
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> Response:
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
