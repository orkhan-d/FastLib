from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, Text
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "Books"

    book_id = Column("book_id", Integer, primary_key = True)

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
    __tablename__ = "Tags"
    tag_id = Column("tag_id", Integer, primary_key=True)
    title = Column("title", String(length=255), nullable=False)

    def __init__(
        self, title: str
    ):
        self.title = title

    def __repr__(self) -> str:
        return f"Tag #{self.tag_id} \"{self.title}\""