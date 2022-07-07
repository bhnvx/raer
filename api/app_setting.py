from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from middleware.middleware import TimeHeaderMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TimeHeaderMiddleware)