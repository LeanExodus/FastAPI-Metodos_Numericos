from fastapi import HTTPException, status
from math import e, pi, cos, sin, tan, sqrt, log, atan
from utils.continuity import test_continuity

#mediante bolzano verifica si entre intervalo ingresado hay una raiz
def bolzano_ver(xa, xb, function: str):
    #Se usa la funcion para verificar la continuidad antes de verificar bolzano
    test_continuity(function,xa,xb)

    if (function(xa) * function(xb) < 0 ):
        return True
    else:
        return False

#mediante bolzano se calcula el intervalo en caso de no ser ingresado
def bolzano_calc(function: str):
    interval = []
    for x in range(-10,51,1):
        
        if bolzano_ver(x,x+1,function):
            interval.append(x)
            interval.append(x+1)
            return interval
        
    raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="No se encuentra una raiz al buscar intervalos con bolzano")        
   
   
        