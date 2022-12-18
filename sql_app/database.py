from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    "sqlite:///./data.db",
    connect_args={"check_same_thread": False}
)
session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()