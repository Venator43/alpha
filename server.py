from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/{command_type}}/{command}")
def read_root(command_type: str, command: str):
    return {"Hello": "World"}