from fastapi import HTTPException, status
from math import e, pi, cos, sin, tan, sqrt, log, atan
from schemas.newton import NewtonOutput
from utils.continuity import test_continuity
from utils.utils import t_func, t_interval, t_derivate_func, middle_point
from utils.bolzano import bolzano_ver, bolzano_calc
from utils.parsedFunc import get_parsed_func
from utils.errorCalc import error_calculation
from utils.derivedFunc import get_derived_func, get_lamb_derived_func
from sympy import *
import numpy as np


#Funcion de newton raphson | Aqui se usan las funciones lambda enviando el valor de x para ser evaluado en las respectivas funciones
def newton_calculation(x, func, derived_func):
  try:
    result = x-(func(x)/derived_func(x))
  except:
      raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Error al realizar el calculo de la iteracion")
  return result


def newton_method(func: str, x: str, xa: str, xb: str, tol: str):
    func = t_func(func)
    derived_func = t_derivate_func(str(get_derived_func(func)))
    derived_func_lamb = get_lamb_derived_func(func)
    func = get_parsed_func(func)
    list_newtonOutput = []
    tol = float(tol)
    current_error = 100 
    iteration = 0
    previous_result = 0

    if xa == '' and xb == '' and x=='':
        print('puntos vacios, se calcula con bolzano el intevalo y se calcula punto medio')
        interval = bolzano_calc(func)
        x = middle_point(interval[0],interval[1])
       
    elif len(xa) > 0 and len(xb) > 0 and x =='':
        print('Hay intervalo se calcula punto medio')
        xa = t_interval(xa)
        xb = t_interval(xb)
        if bolzano_ver(xa,xb,func):
          x = middle_point(xa,xb)
        else:
          raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="No hay una raiz en el intervalo")
        
    elif xa=='' and xb=='' and len(x) > 0:
        print('Hay un punto medio')
        x = t_interval(x)
        test_continuity(func,x)
       

    while current_error > tol and iteration < 50:
        
        current_result = newton_calculation(x,func,derived_func_lamb)
        current_error = error_calculation(current_result,previous_result)
        
        x = current_result
          
        previous_result = current_result
        iteration += 1
          
        list_newtonOutput.append(NewtonOutput(derivative=derived_func,iteration=str(iteration), result=str(current_result), error=str(np.format_float_positional(current_error,trim='-'))))
    return list_newtonOutput

