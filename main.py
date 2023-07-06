from typing import Union

from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    print("server is running ..")
    return {"message": "this is a FastAPI Demo APP"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
