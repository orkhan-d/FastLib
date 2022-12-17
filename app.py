from fastapi import FastAPI
import routers

app = FastAPI()

app.include_router(routers.books.router)
app.include_router(routers.tags.router)

@app.get("/")
def root():
    return {"Response": "Hello World!"}