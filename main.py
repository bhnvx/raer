import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from middleware.middleware import TimeHeaderMiddleware

from router.router import api


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TimeHeaderMiddleware)
app.include_router(api)


@app.get('/')
def Home():
    return "TEST"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)