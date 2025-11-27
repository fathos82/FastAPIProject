from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h1>Eai Galera do Curso do Athos!</h1>"

@app.get("/hello/{name}", response_class=HTMLResponse)
async def say_hello(name: str):
    return f"<h1>hello! {name}</h1>"
