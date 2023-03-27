from typing import Union

from fastapi import FastAPI
from .type_processor import type_processor

app = FastAPI()
procesor = type_processor("C:/Users/ASUS/Documents/Program/Python/AI/Experimental/alpha/config/test2.yml")

@app.get("/{command_type}}/{command}")
def read_root(command_type: str, command: str):
    return procesor.run(command_type, command)