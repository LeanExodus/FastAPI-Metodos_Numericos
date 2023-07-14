from fastapi import APIRouter, status, HTTPException, Depends, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from config.db import conn
from models.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT
from datetime import datetime, timedelta
from typing import Union, Annotated
from jose import jwt, JWTError
import bcrypt

keysalt = bcrypt.gensalt()

user = APIRouter()

oauth2_schema = OAuth2PasswordBearer("/login")

SECRET_KEY = "75f4d68590719c0221085bea67dc48844ccea7a95e921ab7f04334f6356d83fe"
ALGORITHM = "HS256"

#Busca al usuario en la db, en caso de encontrarlo lo retorna y si no retorna una lista vacia
def get_user(username):
    try:
        user_data = conn.execute(users.select().where(users.c.username == username)).first()._mapping
        return User(**user_data)
    except:
        return []

#Verifica la contraseña del usuario
def verify_password(plane_password, hashed_password):
   
    return bcrypt.checkpw(plane_password,hashed_password)

#Autentica al usuario usando las funciones get_user y verify_password
def authenticate_user(username, password):
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No se pueden validar las credenciales", headers= {"WWW-Authenticate": "Bearer"})
    if not verify_password(password.encode("utf-8"), user.password.encode("utf-8")):
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No se pueden validar las credenciales", headers= {"WWW-Authenticate": "Bearer"})
    return user

#Crea el JW Token
def create_token(data: dict, time_expire: Union[datetime,None] = None):
    data_copy = data.copy()
    if time_expire is None:
        expires = datetime.utcnow() + timedelta(minutes=15)
    else:
        expires = datetime.utcnow() + time_expire
    data_copy.update({"exp": expires})
    token_jwt = jwt.encode(data_copy, key = SECRET_KEY, algorithm= ALGORITHM)
    return token_jwt

#Verifica que el usuario logueado sea el mismo de jwt token
def get_current_user(token: str = Depends(oauth2_schema)):
    try:
        token_decode = jwt.decode(token, key= SECRET_KEY, algorithms=[ALGORITHM])
        username = token_decode.get("sub")
        if username == None:
             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No se pueden validar las credenciales", headers= {"WWW-Authenticate": "Bearer"})
    except JWTError:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No se pueden validar las credenciales", headers= {"WWW-Authenticate": "Bearer"})
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No se pueden validar las credenciales", headers= {"WWW-Authenticate": "Bearer"})
    return user

#Obtener el usuario logueado
@user.get("/users/me", tags=["users"])
def get_auth_user(current_user: User = Depends(get_current_user)):
    return current_user


@user.post("/login", tags=["Login"])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_auth = authenticate_user(form_data.username, form_data.password)
    access_token_expires = timedelta(minutes=40)
    access_token_jwt = create_token({"sub": user_auth.username}, access_token_expires)
    return {
        "access_token": access_token_jwt,
        "token_type": "bearer"
    }

#Registrar Usuario
@user.post("/users", response_model=User, tags=["users"])
def create_user(user: User):
    #Hacemos diccionario a nuestro usuario
    new_user = user.dict()
    #Encriptamos la contraseña del usuario y se lo pasamos al diccionario
    new_user["password"] = bcrypt.hashpw(user.password.encode("utf-8"),keysalt)


    #Hacemos la insercion del usuario en la DB y con el commit enviamos la transaccion
    try:
        result = conn.execute(users.insert().values(new_user))
        conn.commit()
    except:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Usuario ya existe")
    
    #Devolvemos el usuario agregado mediante otra transaccion y en forma de diccionario
    return  conn.execute(users.select().where(users.c.id == result.lastrowid)).first()._mapping

#Eliminar Usuario
@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str, token: Annotated[str, Depends(oauth2_schema)]):
    #Eliminamos el usuario indicado por el id y enviamos la transaccion 
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()

    return Response(status_code=HTTP_204_NO_CONTENT)

#Actualizar usuario
@user.put("/users/{id}", response_model=User, tags=["users"])
def update_user(id: str, user: User, token: Annotated[str, Depends(oauth2_schema)]):

    #Actualizamos el usuario indicado por el id y enviamos la transaccion
    try:
        conn.execute(users.update().values(username = user.username, password = bcrypt.hashpw(user.password.encode("utf-8"))).where(users.c.id == id))
        conn.commit()
    except:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ese username ya esta en uso")
   #Devolvemos el usuario agregado mediante otra transaccion y en forma de diccionario
    return  conn.execute(users.select().where(users.c.id == id)).first()._mapping

"""@user.get("/users/{id}", response_model=User, tags=["users"])
def get_user_route(id: str, token: Annotated[str, Depends(oauth2_schema)]):
     

     #Devolvemos el usuario buscado en forma de diccionario
     return conn.execute(users.select().where(users.c.id == id)).first()._mapping"""