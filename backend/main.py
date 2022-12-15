from fastapi import FastAPI,File
from starlette.responses import Response
import io
data = {20,30,10}



app = FastAPI()



@app.post("/results")
def results():
    return data