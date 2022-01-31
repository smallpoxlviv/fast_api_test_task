from fastapi import FastAPI
import uvicorn

from settings import settings
from api import router


app = FastAPI()
app.include_router(router)

@app.get('/')
def root():
    return {'message': 'root page'}


if __name__ == "__main__":
    uvicorn.run(
    "app:app", 
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)