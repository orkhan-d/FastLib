from fastapi import APIRouter, Query, Depends, File, UploadFile

from sql_app.crud import Session
from sql_app import crud, database, schemas

from exceptions import BookAlreadyExists, WrongBookType

router = APIRouter()

@router.post('/books/new', tags=['Books'])
def add_book(
    title: str, author: str, description: str = None, file: UploadFile = File(), book_tags: list[str] = Query(None),
    db: Session = Depends(database.get_db)):
    try:
        if not any ([file.filename.endswith(book_type) \
            for book_type in [
                'fb2', 'doc', 'docx', 'txt', 'epub'
            ]]):
            raise WrongBookType

        crud.create_book(
            db, schemas.BookCreate(
                title=title,
                author=author,
                description=description,
                file=file.filename,
                tags=book_tags
            ), file.file
        )
        return {
            "Title": title,
            "Author": author,
            "Description": description,
            "Tags": book_tags
        }
    except BookAlreadyExists:
        return {
            "Error": "Book already exists!"
        }
    except WrongBookType:
        return {
            "Error": "Wrong book type!"
        }