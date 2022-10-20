from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


from app.api.v1.api import api_router
from app.core.config import db_settings


settings = db_settings
app = FastAPI(title="medusa")


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
