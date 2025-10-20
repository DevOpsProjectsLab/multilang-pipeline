from pydantic import BaseModel, Field

class TodoIn(BaseModel):
    title: str = Field(min_length=1)

class TodoOut(BaseModel):
    id: str
    title: str
    done: bool
