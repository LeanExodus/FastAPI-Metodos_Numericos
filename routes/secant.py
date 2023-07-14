from fastapi import APIRouter, Depends
from schemas.secant import SecantInput,SecantOutput
from services.secant import secant_method
from typing import Annotated
from routes.user import oauth2_schema

secant = APIRouter()



@secant.post("/secant",response_model=list[SecantOutput], tags=["Secant"])
def secant_calculator(secant_input: SecantInput, token: Annotated[str, Depends(oauth2_schema)]):
    func = secant_input.func
    xa = secant_input.xa
    xb = secant_input.xb
    tol = secant_input.tolerance

    return secant_method(func,xa,xb,tol)

    
