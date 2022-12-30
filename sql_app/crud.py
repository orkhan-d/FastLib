from sqlalchemy.orm import Session
from sqlalchemy import and_

from . import models, schemas
from exceptions import BookAlreadyExists

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.book(
        title=book.title,
        author=book.author,
        description=book.description
    )

    if not db.query(models.book).filter(
        and_(
            models.book.title==book.title,
            models.book.author==book.author
        )
    ).first():
        db.add(db_book)
        db.commit()

        for tag in book.tags:
            db_tag = models.tag(tag)

            if not db.query(models.tag).filter(
                models.tag.title==tag
            ).first():
                db.add(db_tag)
                db.commit()
            else:
                db_tag = db.query(models.tag).filter(
                    models.tag.title==tag
                ).first()

            db_book_tag = models.book_tag(db_book.book_id, db_tag.tag_id)
            db.add(db_book_tag)
            db.commit()
    else:
        raise BookAlreadyExists