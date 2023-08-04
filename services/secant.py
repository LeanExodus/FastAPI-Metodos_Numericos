from fastapi import HTTPException, status
from math import e, pi, cos, sin, tan, sqrt, log, atan
from schemas.secant import SecantOutput
from utils.bolzano import bolzano_ver, bolzano_calc
from utils.utils import t_func, t_interval
from utils.parsedFunc import get_parsed_func
from utils.errorCalc import error_calculation
from sympy import *


#Funcion de secante | Aqui se usa la funcion lambda enviando el valor de xa o xb segun corresponda con la formula
def secant_calculation(xa, xb, func):
  try:
      result = (xb - ((func(xb) * (xb - xa)) / (func(xb) - func(xa))))
  except:
      raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Error al realizar el calculo de la iteracion")
  return result


def secant_method(func: str, xa: str, xb: str, tol: str):
    func = t_func(func)
    func = get_parsed_func(func)
    list_secantOutput = []
    tol = float(tol)
    current_error = 100 
    iteration = 0
    previous_result = 0

    if xa == '' and xb == '':
        print('puntos vacios, se calcula con bolzano el intevalo')
        interval = bolzano_calc(func)
        xa = interval[0]
        xb = interval[1]
    else:
        print('si hay puntos')
        xa = t_interval(xa)   
        xb = t_interval(xb)
        if not bolzano_ver(xa,xb,func):
            raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="No hay una raiz en el intervalo")

    while current_error > tol and iteration < 50:
        
        current_result = secant_calculation(xa,xb,func)
        current_error = error_calculation(current_result,previous_result)

        if func(current_result) < xb:
            xa = current_result
        else: 
            xb = current_result
                
        previous_result = current_result
        iteration += 1

        list_secantOutput.append(SecantOutput(iteration=str(iteration), result=str(current_result), error=str(("%.17f" % current_error).rstrip('0').rstrip('.'))))
        
    return list_secantOutput