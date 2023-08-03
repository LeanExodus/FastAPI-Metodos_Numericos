from fastapi import HTTPException, status

#Calcula el error en cada iteracion
def error_calculation(current, previous) -> float:
  try:
      result = abs(((current - previous) / current) * 100)
  except:
      raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Calculo de error invalido")
  return result