from typing import Optional
from sqlmodel import SQLModel, Field


class Board(SQLModel, table=True):
    id = None