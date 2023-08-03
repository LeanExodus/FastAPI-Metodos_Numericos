#En caso de ingresar un valor como fraccion (3/4) lo divide y lo almacena como su valor float
def t_interval(x: str):
    if ('/' in x):
        listx = x.split('/')
        x = float(listx[0]) / float(listx[1])
        return float(x)
    elif (',' in x):
        x = x.replace(',','.')
        return float(x)
    else:
        return float(x)

#En caso de que la funcion ingresada contenga el simbolo ^ para expresar potencia lo transforma en el valor valido de potencia ** de python
def t_func(func: str):
    if ('^' in func):
        func = func.replace('^', '**')
        return func 
    else:
        return func
    
#Cambia el simbolo ** del resultado de la derivada por ^ para comprenderlo mejor  
def t_derivate_func(func: str):
    if ('**' in func):
        func = func.replace('**', '^')
        return func 
    else:
        return func
    

#sympy entiende a euler como 'E' asi que al ingresar 'e' tenemos que cambiarlo
def e_changer(func: str):
    if ('e' in func):
        func = func.replace('e','E')
        return func
    else:
        return func

#Calcula el punto medio dado un intervalo
def middle_point(xa: str, xb: str):
    return (xa+xb)/2