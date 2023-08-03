from fastapi import HTTPException, status
from math import e, pi, cos, sin, tan, sqrt, log, atan
from utils.utils import e_changer
#Sympy se usa para obtener la derivada de la funcion
from sympy import *


#Calcula la derivada de la funcion y la transforma en una ecuacion valida para remplazar x
def get_lamb_derived_func(function: str):
    x = symbols('x')
    function = e_changer(function)
    try:
        derived_func = diff(function,x)
    except:
         raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail="Error al calcular la derivada de la funcion lambda")
    return lambdify(x,derived_func)

#Calcula la derivada de la funcion y la retorna (se utiliza para la impresion de la derivada)
def get_derived_func(function: str):
    x = symbols('x')
    function = e_changer(function)
    try:
        derived_func = diff(function,x)
    except:
         raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail="Error al calcular la derivada de la funcion")
    return derived_func

