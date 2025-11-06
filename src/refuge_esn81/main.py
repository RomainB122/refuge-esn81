from typing import Union
import uvicorn

from fastapi import FastAPI
from refuge_esn81.router.animals import animalsRouter

app = FastAPI()
app.include_router(animalsRouter)

if __name__ == '__main__':
    uvicorn.run(app, port=9000)
