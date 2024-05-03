import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import api

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api.router)

#INICIAR UVICORN (SERVIDOR LOCAL DONDE SE PUEDE VISUALIZAR LA INTERFAZ WEB)
if __name__ == '__main__':
    uvicorn.run(app)