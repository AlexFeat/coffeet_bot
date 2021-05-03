#!/usr/bin/env python
import uvicorn
from fastapi import FastAPI
from routers import root

app = FastAPI()

app.include_router(root.router)

if __name__ == '__main__':
    print('Just start!')
    uvicorn.run(app, host="0.0.0.0", port=8000)
