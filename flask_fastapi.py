from fastapi import FastAPI, Request
from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn
from flask import Flask, render_template


#init fastapi
app = FastAPI()
#init flask
flask_app = Flask(__name__)
#connect flask with fast
app.mount("/home", WSGIMiddleware(flask_app))


@flask_app.get("/")
def home_page():
    return render_template('homepage.html')


@app.get("/")
def read_root():
    return {'text':"Fastapi section"}


if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)