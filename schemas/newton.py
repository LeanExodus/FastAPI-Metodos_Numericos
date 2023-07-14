from pydantic import BaseModel
from typing import Optional
from math import e, pi, cos, sin, tan, sqrt
#Sympy se usa para obtener la derivada de la funcion
from sympy import *


class NewtonInput(BaseModel):
    func: str
    x: Optional[str]
    tolerance: Optional[str]


class NewtonOutput(BaseModel):
    iteration: str
    result: str
    error: str

