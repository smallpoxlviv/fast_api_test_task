import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

from settings import settings
from api import router
from api.auth import is_token_valid
 

app = FastAPI()
app.include_router(router)

@app.get('/')
def root():
    return {'message': 'root page'}

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if is_token_valid(form_data.password):
        return {"access_token": settings.super_secret_token, "token_type": "bearer"}


if __name__ == "__main__":
    uvicorn.run(
    "app:app", 
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)