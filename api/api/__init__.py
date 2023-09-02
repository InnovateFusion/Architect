from fastapi import FastAPI
from .routes.user import router as user_router
from .routes.home import router as home_router
from .common import models
from .common.database import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(home_router, prefix="/api/v1", tags=["homes"])
app.include_router(user_router, prefix="/api/v1", tags=["users"]) 








    