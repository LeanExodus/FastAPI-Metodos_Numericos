from pydantic import BaseModel
from typing import Optional

class SecantInput(BaseModel):
    func: str
    xa: Optional[str]
    xb: Optional[str]
    tolerance: Optional[str]


class SecantOutput(BaseModel):
    iteration: str
    result: str
    error: str




