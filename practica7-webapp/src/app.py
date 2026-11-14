import os
from flask import Flask
import mysql.connector

app = Flask(__name__)

def obtener_mensaje():
    # Los datos de conexión se leen de variables de entorno (definidas en docker-compose.yml).
    # Así el código no queda atado a una contraseña o servidor específico.
    conexion = mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT texto FROM mensajes LIMIT 1")
    texto = cursor.fetchone()[0]
    # Se cierran cursor y conexión para no dejar conexiones abiertas en el servidor
    cursor.close()
    conexion.close()
    return texto

@app.route("/")
def inicio():
    return f"<h1>{obtener_mensaje()}</h1>"