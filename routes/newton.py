from fastapi import APIRouter, Depends
from schemas.newton import NewtonInput,NewtonOutput
from services.newton import newton_method
from typing import Annotated
from routes.user import oauth2_schema

newton = APIRouter()



@newton.post("/newton",response_model=list[NewtonOutput] , tags=["Newton"])
def newton_calculator(newton_input: NewtonInput, token: Annotated[str, Depends(oauth2_schema)]):
    func = newton_input.func
    x = (newton_input.x)
    tol = (newton_input.tolerance)

    return newton_method(func,x,tol)
