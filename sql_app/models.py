from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, Text
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "Books"

    book_id = Column("Book_id", Integer, primary_key = True)

    title = Column("Title", String(length=255), nullable = False)
    author = Column("Author", String(length=255))

    description = Column("Description", Text, nullable=True)

    def __init__(
        self, title: str, author: str, description: str = None
    ):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self) -> str:
        return f"\"{self.title}\", {self.author}"