from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/time")
def root():
    return { "time": datetime.now() }
