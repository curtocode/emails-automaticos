import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(sender_email, receiver_email, password):
    port = 465  # Puerto para SSL
    smtp_server = 'smtp.gmail.com'
    
    # Crear el mensaje
    message = MIMEMultipart("alternative")
    message["Subject"] = "Incidencia panelais linea 1"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Crear el cuerpo del correo en formato HTML
    html = f"""
    <html>
      <body>
      Hola, <i>{receiver_email}</i><br>
      Espero que estés bien.<br>
      <body>
    </html>"""
    
    # Adjuntar la parte HTML
    parte_html = MIMEText(html, "html")
    message.attach(parte_html)


    # Conexión segura con el servidor
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email enviado")
