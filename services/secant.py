from schemas.secant import SecantOutput
from utils.utils import t_func, t_interval
from math import e, pi, cos, sin, tan, sqrt

#Nos permite tranformar la funcion ingresada en una funcion valida para remplazar x
#Eval() nos permite evaluar una funcion ingresada (str) y devolver su valor
#Lambda nos permite transformar la funcion evaluda en una ecuacion valida para remplazar x
def get_parsed_func(function: str):
        return lambda x: eval(function)

#Funcion de secante | Aqui se usa la funcion lambda enviando el valor de xa o xb segun corresponda con la formula
def secant_calculation(xa, xb, func):
  return (xb - ((func(xb) * (xb - xa)) / (func(xb) - func(xa))))

#Calcula el error en cada iteracion
def error_calculation(current, previous) -> float:
  return abs(((current - previous) / current) * 100)


def secant_method(func: str, xa: str, xb: str, tol: str):
    func = t_func(func)

    #Hacer try cath aqui
    func = get_parsed_func(func)
    #Hacer try cath aqui
    xa = t_interval(xa)
    #Hacer try cath aqui
    xb = t_interval(xb)
    tol = float(tol)
    current_error = 100 
    iteration = 0
    previous_result = 0
    list_secantOutput = []

    while current_error >= tol:
        #Hacer try cath aqui
        current_result = secant_calculation(xa,xb,func)
        #Hacer try cath aqui
        current_error = error_calculation(current_result,previous_result)

        if func(current_result) < xb:
            xa = current_result
        else:
            xb = current_result
        
        previous_result = current_result
        iteration += 1

        print(iteration,"|",current_result," Error=",current_error,"%")
        list_secantOutput.append(SecantOutput(iteration=str(iteration), result=str(current_result), error=str(current_error)))
    return list_secantOutput