from fastapi import FastAPI
import routers

app = FastAPI()

app.include_router(routers.books.router)
app.include_router(routers.tags.router)

from sql_app.database import Base, engine

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"Response": "Hello World!"}