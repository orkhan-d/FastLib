from sqlalchemy.orm import Session
from . import models, schemas

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.book(
        title=book.title,
        author=book.author,
        description=book.description
    )
    db.add(db_book)
    db.flush()

    for tag in book.tags:
        db_tag = models.tag(tag)

        db.add(db_tag)
        db.flush()

        db_book_tag = models.book_tag(db_book.book_id, db_tag.tag_id)
        db.add(db_book_tag)

        db.flush()

    db.commit()