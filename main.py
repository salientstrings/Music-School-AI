from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Music School AI Assistant Running"}