from pydantic import BaseModel

# Books
class BookBase(BaseModel):
    title: str
    author: str
    description: str | None = None
    tags: list[str] | None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    book_id: int

    class Config:
        orm_mode = True

# Tags
class TagBase(BaseModel):
    title: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    tag_id: int

    class Config:
        orm_mode = True

# Book tags
class BookTagBase(BaseModel):
    tag_id: int
    book_id: int

class BookTagCreate(BookTagBase):
    pass

class BookTag(BookTagBase):
    
    class Config:
        orm_mode = True