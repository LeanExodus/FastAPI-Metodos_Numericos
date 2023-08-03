from fastapi import HTTPException, status
from math import e, pi, cos, sin, tan, sqrt, log, atan

#verifica la continuidad de la funcion en 0 y los puntos
def test_continuity(func: str, xa: str = '-10', xb: str = '10'):
    try:
      func(0)
    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Funcion discontinua en: 0")
    try:
       func(float((xa)))
    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Funcion discontinua en: {xa}")
    try:
        func(float((xb)))
    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Funcion discontinua en: {xb}")
