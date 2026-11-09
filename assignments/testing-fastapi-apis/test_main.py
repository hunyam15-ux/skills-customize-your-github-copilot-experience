import pytest
from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_books(monkeypatch):
    monkeypatch.setattr(
        main,
        "books",
        [
            main.Book(id=1, title="The Hobbit", author="J. R. R. Tolkien", published_year=1937),
            main.Book(id=2, title="Frankenstein", author="Mary Shelley", published_year=1818),
        ],
    )
    monkeypatch.setattr(main, "_next_book_id", 3)


def test_list_books():
    response = client.get("/books")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["title"] == "The Hobbit"


def test_get_book():
    response = client.get("/books/2")

    assert response.status_code == 200
    assert response.json()["title"] == "Frankenstein"


# Add tests for creating, updating, and deleting books.
# Add tests for missing book IDs and invalid request data.
