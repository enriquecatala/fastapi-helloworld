"""
 Contact me:
   e-mail:   enrique@enriquecatala.com 
   Linkedin: https://www.linkedin.com/in/enriquecatala/
   Web:      https://enriquecatala.com
   Twitter:  https://twitter.com/enriquecatala
   Support:  https://github.com/sponsors/enriquecatala
   Youtube:  https://www.youtube.com/enriquecatala
   
"""
from os import environ
import json
from typing import Optional
from loguru import logger

from fastapi import FastAPI

app = FastAPI()


@app.get("/one/hello")
def read_root():
    if "HELLOWORLD_ENV" in environ:
        txt = environ.get('HELLOWORLD_ENV')
    else:
        txt = "HELLOWORLD_ENV not found!"
    return {"HELLOWORLD_ENV: {}".format(txt): "from /one/hello"}


@app.get("/get_api_key")
def read_api_key():
    api_key = ""    
    
    try:
        with open('/app/secrets/appconfig.conf') as f:
            js = json.load(f)
            api_key = js["api_key"]
            # Do something with the file

    except IOError:
        logger.exception(e)
        print("/app/secrets/appconfig.conf not accessible")

    return {"API_KEY: {}".format(api_key)}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
