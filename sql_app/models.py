from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, Text
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "Books"

    book_id = Column("Book_id", Integer, primary_key = True)

    title = Column("Title", String(length=255), nullable = False)
    description = Column("Description", Text, nullable=True)

    author = Column("Author", String(length=255))