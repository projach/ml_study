from fastapi import FastAPI, Request
from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn


#init fastapi
app = FastAPI()

@app.get("/")
def read_root():
    return {'text':"Fastapi section"}


if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)