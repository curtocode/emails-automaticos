from fastapi import FastAPI
from pydantic import BaseModel
from email_sender import enviar_email

 # Importamos la función del módulo

app = FastAPI()

# Definimos el esquema para recibir los datos del correo
class EmailRequest(BaseModel):
    sender_email: str
    receiver_email: str
    password: str

@app.post("/enviar_email")
async def enviar_correo(datos: EmailRequest):
    enviar_email(
        sender_email=datos.sender_email,
        receiver_email=datos.receiver_email,
        password=datos.password,
    )
    return {"message": "Correo enviado correctamente"}
