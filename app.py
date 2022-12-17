from fastapi import FastAPI
import routers

app = FastAPI()

app.include_router(routers.books.router)
app.include_router(routers.tags.router)

import sql_app

sql_app.database.Base.metadata.create_all(bind=sql_app.database.engine)

@app.get("/")
def root():
    return {"Response": "Hello World!"}