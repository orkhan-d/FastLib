from fastapi import APIRouter, Query, Depends

from sql_app.crud import Session
from sql_app import crud, database, schemas

from exceptions import BookAlreadyExists

router = APIRouter()

@router.post('/books/new', tags=['Books'])
def add_book(
    title: str, author: str, description: str = None,  book_tags: list[str] = Query(None),
    db: Session = Depends(database.get_db)):
    try:
        crud.create_book(
            db, schemas.BookCreate(
                title=title,
                author=author,
                description=description,
                tags=book_tags
            )
        )
        return {
            "Title": title,
            "Author": author,
            "Description": description,
            "Tags": book_tags
        }
    except BookAlreadyExists:
        return {
            "Error": "Book already exists"
        }