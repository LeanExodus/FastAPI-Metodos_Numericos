from fastapi import FastAPI
from routes.user import user
from routes.secant import secant
from routes.newton import newton

app = FastAPI(
    openapi_tags=[{
        "title": "REST-API Metodos Numericos",
        "name": "users",
        "description": "users routes"
    }]
)

app.include_router(user)
app.include_router(secant)
app.include_router(newton)