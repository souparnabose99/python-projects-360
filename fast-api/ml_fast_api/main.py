from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def main():
    return {"message": "Base Url"}


# /name endpoint
@app.get("/{name}")
def page_name(name: str):
    return {"message": f"Welcome to !, {name}"}

