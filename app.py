from fastapi import FastAPI
from routes.user import user
from routes.secant import secant
from routes.newton import newton
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    openapi_tags=[{
        "title": "REST-API Metodos Numericos",
        "name": "users",
        "description": "users routes"
    }]
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(secant)
app.include_router(newton)
