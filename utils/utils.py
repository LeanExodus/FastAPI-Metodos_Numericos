#En caso de ingresar un valor como fraccion (3/4) lo divide y lo almacena como su valor float
def t_interval(x: str):
    if ('/' in x):
        listx = x.split('/')
        x = float(listx[0]) / float(listx[1])
        return float(x)
    else:
        return float(x)

#En caso de que la funcion contenga el simbolo ^ para expresar potencia lo transforma en el valor valido de potencia ** de python
def t_func(func: str):
    if ('^' in func):
        func = func.replace('^', '**')
        return func 
    else:
        return func