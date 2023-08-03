from pydantic import BaseModel
from typing import Optional

class NewtonInput(BaseModel):
    func: str
    x: Optional[str]
    xa: Optional[str]
    xb: Optional[str]
    tolerance: Optional[str]


class NewtonOutput(BaseModel):
    derivative: str
    iteration: str
    result: str
    error: str

