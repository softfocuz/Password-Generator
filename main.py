from fastapi import FastAPI
from routers.root import router

app = FastAPI()
app.include_router(router)