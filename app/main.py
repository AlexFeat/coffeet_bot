#!/usr/bin/env python

import uvicorn
from fastapi import FastAPI
from app.routers import root, callback
from app.models import database


app = FastAPI()

app.include_router(root.router)
app.include_router(callback.telegram.router)


@app.on_event("startup")
async def startup_event():
    print('Startup actions')
    await database.connect()


@app.on_event("shutdown")
async def shutdown_event():
    print('Shutdown actions')


if __name__ == '__main__':
    print('Just start!')
    uvicorn.run(app, host="0.0.0.0", port=8000)
