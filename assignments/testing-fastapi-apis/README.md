# 📘 Assignment: Testing FastAPI APIs

## 🎯 Objective

Write automated tests for a FastAPI application using `pytest` and FastAPI's `TestClient`. Verify successful CRUD operations, error responses, and request validation without running a web server.

## 📝 Tasks

### 🛠️ Test Read Endpoints

#### Description
Use the provided book API and test scaffold to check that clients can list books and retrieve a book by ID.

#### Requirements
Completed program should:

- Install FastAPI, pytest, and HTTPX with `python -m pip install fastapi pytest httpx`.
- Run tests with `python -m pytest -v`.
- Check that `GET /books` returns HTTP 200 and the expected book data.
- Check that `GET /books/{book_id}` returns HTTP 200 and the requested book.
- Keep each test independent by resetting the in-memory book data before each test.

### 🛠️ Test CRUD Behavior

#### Description
Add tests that verify creating, updating, and deleting books changes the API's data as expected.

#### Requirements
Completed program should:

- Check that `POST /books` returns HTTP 201 and the created book, including its ID.
- Check that `PUT /books/{book_id}` returns the updated book and that the update persists.
- Check that `DELETE /books/{book_id}` returns HTTP 204 and the book is no longer available.
- Assert both response status codes and relevant response data.

### 🛠️ Test Errors and Validation

#### Description
Test how the API responds to unknown book IDs and invalid request data.

#### Requirements
Completed program should:

- Check that reading, updating, or deleting a missing book returns HTTP 404.
- Check that a `POST /books` request with a missing required field returns HTTP 422.
- Check that the test suite passes with `python -m pytest -v`.
