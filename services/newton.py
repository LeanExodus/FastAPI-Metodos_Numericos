from schemas.newton import NewtonOutput
from utils.utils import t_func, t_interval
from math import e, pi, cos, sin, tan, sqrt
#Sympy se usa para obtener la derivada de la funcion
from sympy import *


#Nos permite tranformar la funcion ingresada en una funcion valida para remplazar x
#Eval() nos permite evaluar una funcion ingresada (str) y devolver su valor
#Lambda nos permite transformar la funcion evaluda en una ecuacion valida para remplazar x
def get_parsed_func(function: str):
        return lambda x: eval(function)

#Calcula la derivada de la funcion y la transforma en una ecuacion valida para remplazar x
def get_derived_func(function: str):
    x = symbols('x')
    derived_func = diff(function,x)
    return lambdify(x,derived_func)

#Funcion de newton raphson | Aqui se usan las funciones lambda enviando el valor de x para ser evaluado en las respectivas funciones
def newton_calculation(x, func, derived_func):
  return x-(func(x)/derived_func(x))

#Calcula el error en cada iteracion
def error_calculation(current, previous) -> float:
  return abs(((current - previous) / current) * 100)

def newton_method(func: str, x: str, tol: str):
    func = t_func(func)
    
    try:
        derived_func = get_derived_func(func)
    except Exception as error:
        print("Ingresa una funcion valida:", error)

    try:
        func = get_parsed_func(func)
    except Exception as error:
        return ("Ingresa una funcion valida:", error)
    
    try:
        x = t_interval(x)
    except Exception as error:
        print("Ingresa un punto valido:", error)

    tol = float(tol)
    current_error = 100 
    iteration = 0
    previous_result = 0
    list_newtonOutput = []

    while current_error >= tol:
        try:
            current_result = newton_calculation(x,func,derived_func)
        except Exception as error:
            print("Error al calcular newtonRaphson:", error)
            return ("Error al calcular newtonRaphson:", error)

        try:
            current_error = error_calculation(current_result,previous_result)
        except Exception as error:
            print("Error al calcular el error %:", error)

        x = current_result
        
        previous_result = current_result
        iteration += 1

        print(iteration,"|",current_result," Error=",current_error,"%")
        list_newtonOutput.append(NewtonOutput(iteration=str(iteration), result=str(current_result), error=str(current_error)))
    return list_newtonOutput