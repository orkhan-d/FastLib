from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, Text
from sqlalchemy.orm import relationship
from .database import Base

class book(Base):
    __tablename__ = "books"

    book_id = Column("id", Integer, primary_key = True)

    title = Column("title", String(length=255), nullable = False)
    author = Column("author", String(length=255), nullable = False)

    description = Column("description", Text, nullable=True)

    def __init__(
        self, title: str, author: str, description: str = None
    ):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self) -> str:
        return f"\"{self.title}\", {self.author}"

class tag(Base):
    __tablename__ = "tags"

    tag_id = Column("id", Integer, primary_key=True)
    title = Column("title", String(length=255), nullable=False)

    def __init__(
        self, title: str
    ):
        self.title = title

    def __repr__(self) -> str:
        return f"Tag #{self.tag_id} \"{self.title}\""

class book_tag(Base):
    __tablename__ = "book_tags"

    book_id = Column("book_id", ForeignKey('books.id'), primary_key=True)
    tag_id = Column("tag_id", ForeignKey('tags.id'), primary_key=True)

    def __init__(
        self, book_id: int, tag_id: int
    ):
        self.book_id = book_id
        self.tag_id = tag_id

    def __repr__(self) -> str:
        return f"Book #{self.book_id} has tag #{self.tag_id}"
