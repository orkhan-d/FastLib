from sqlalchemy.orm import Session
from sqlalchemy import and_

from . import models, schemas
from exceptions import BookAlreadyExists

import shutil
import books
import os.path

print(books.__file__)

BOOKS_DIR = '/'+os.path.join(*books.__file__.split('/')[:-1])

def create_book(db: Session, book: schemas.BookCreate, file):
    db_book = models.book(
        title=book.title,
        author=book.author,
        description=book.description,
        file=book.file
    )

    if not db.query(models.book).filter(
        and_(
            models.book.title==book.title,
            models.book.author==book.author,
            models.book.file==book.file
        )
    ).first():
        db.add(db_book)
        db.commit()

        with open(os.path.join(BOOKS_DIR, book.file), 'wb') as buff:
            shutil.copyfileobj(file, buff)

        if not book.tags: return
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