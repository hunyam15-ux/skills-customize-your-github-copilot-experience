# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI to practice defining data models, handling HTTP requests, and returning appropriate responses. Use the interactive API documentation to test your endpoints.

## 📝 Tasks

### 🛠️ Create the Book API

#### Description
Set up the FastAPI application and create endpoints for listing books and retrieving one book by its ID.

#### Requirements
Completed program should:

- Define a book with an integer `id`, a `title`, an `author`, and a `published_year`.
- Store books in an in-memory collection initialized with at least two books.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return the matching book or an HTTP 404 response if it does not exist.

### 🛠️ Add Books

#### Description
Add an endpoint that accepts book details as a JSON request body and adds the new book to the collection.

#### Requirements
Completed program should:

- Implement `POST /books` using a request model that contains the title, author, and published year.
- Assign each new book a unique integer ID.
- Return the newly created book with HTTP status 201.
- Make the new book available from `GET /books` and `GET /books/{book_id}`.

### 🛠️ Update and Remove Books

#### Description
Complete the API by adding endpoints to replace a book's details and remove a book from the collection.

#### Requirements
Completed program should:

- Implement `PUT /books/{book_id}` to update the title, author, and published year of an existing book.
- Implement `DELETE /books/{book_id}` to remove an existing book and return HTTP status 204.
- Return an HTTP 404 response when either endpoint receives an ID that does not exist.
- Run the application with Uvicorn and test each endpoint using FastAPI's interactive documentation at `/docs`.

