from math import e, pi, cos, sin, tan, sqrt, log, atan

#Nos permite tranformar la funcion ingresada en una funcion valida para remplazar x
#Eval() nos permite evaluar una funcion ingresada (str) y devolver su valor
#Lambda nos permite transformar la funcion evaluda en una ecuacion valida para remplazar x
def get_parsed_func(function: str):
        return lambda x: eval(function)