from fastapi import APIRouter, Request, Depends, HTTPException, status, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.esquemas import DatosAutenticacion
from bson import ObjectId
from datetime import datetime
from pymongo.errors import PyMongoError
from api.DB import collection_1
from api.DB import collection_2
from api.DB import collection_3
from api.esquemas import DatosMatricula
from api.esquemas import matriculasEsquema
import os

router = APIRouter(prefix="/proyecto-c", tags=["proyecto-c"])
router.mount("/static", StaticFiles(directory="static"), name="static")
plantillas = Jinja2Templates(directory="web")
UPLOAD_FOLDER = "uploads"

#FUNCION PARA REALIZAR LA VALIDACION DE USUARIO
def buscarUsuario(usuario: str, contrasena: str):
    usuarioEncontrado = collection_3.find_one({"usuario": usuario})
    if usuarioEncontrado is None:
        return False
    elif usuarioEncontrado["contrasena"] != contrasena:
        return False
    else:
        return True

#MÉTODO PARA MOSTRAR LA INTERFAZ WEB DE LOGIN
@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return plantillas.TemplateResponse("login.html", {"request": request})

#MÉTODO PARA ENVIAR LOS DATOS INGRESADOS EN EL LOGIN Y VALIDAR
@router.post("/login/success", response_class=HTMLResponse)
async def validarFormulario(request: Request, datosFormulario: DatosAutenticacion = Depends(DatosAutenticacion.as_form)):
    usuarioAdmin = buscarUsuario(datosFormulario.usuario, datosFormulario.contrasena)
    if not usuarioAdmin:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticaciï¿½n invï¿½lidas.")
    
    return plantillas.TemplateResponse("admin.html", {"request": request})

#MÉTODO PARA MOSTRAR LA INTERFAZ WEB ADMINISTRADOR
@router.get("/login/success", response_model=list[DatosMatricula])
async def listaMatriculas():
    return matriculasEsquema(collection_1.find())