# FastAPI Email Sender

Este proyecto es una API basada en FastAPI que permite enviar correos electrónicos con un archivo adjunto de manera sencilla. El servicio permite personalizar el remitente, destinatario, contraseña y archivo adjunto. 

## Características

- Envío de correos electrónicos a través de Gmail utilizando un servidor SMTP seguro.
- Posibilidad de adjuntar un archivo en el correo.
- Fácil integración con Postman u otras herramientas de testing de APIs.
- Utiliza FastAPI para la creación de endpoints RESTful y Pydantic para la validación de datos.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado lo siguiente:

- Python 3.8 o superior
- FastAPI
- Uvicorn
- smtplib (incluido en la biblioteca estándar de Python)
- Pydantic
- Postman (opcional, para probar la API)

## Instalación
- Se recomienda la instalacion de un entorno virtual "python -m venv venv" e instalar el archivo requirements.txt
- Para hacer correr el servidor usar "uvicorn main:app --reload" en el directorio donde este el main.py
1. **Clona el repositorio**:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio


