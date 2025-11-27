from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return  "<h1>Eai Galera do Curso do Athos!</h1>"


@app.get("/hello/{name}")
async def say_hello(name: str):
    return f"<h1>hello! {name}</h1>"
