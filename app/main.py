from os import environ
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/one/hello")
def read_root():
    if "HELLOWORLD_ENV" in environ:
        txt = environ.get('HELLOWORLD_ENV')
    else:
        txt = "HELLOWORLD_ENV not found!"
    return {"HELLOWORLD_ENV: {}".format(txt): "from /one/hello"}


@app.get("/two/hello")
def read_root():
    if "HELLOWORLD_ENV" in environ:
        txt = environ.get('HELLOWORLD_ENV')
    else:
        txt = "HELLOWORLD_ENV not found!"
    return {"HELLOWORLD_ENV: {}".format(txt): "from /two/hello"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
