from pydantic import BaseModel


labels = {
    0: 'electric',
    1: 'inorganic',
    2: 'organic',
}


class Label(BaseModel):
    id: int
    name: str
