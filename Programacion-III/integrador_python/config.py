import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Esto carga las variables del archivo .env
load_dotenv()
print(f"DEBUG: Host={os.getenv('DB_HOST')}")
print(f"DEBUG: Password={os.getenv('DB_PASSWORD')}")

class DatabaseConfig:
    @staticmethod
    def get_connection():
        try:
            # Aquí usamos variables de entorno (más seguro)
            connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                database=os.getenv('DB_NAME', 'clinica_db'),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD'), # <--- ESTO LEE TU .env
                port='3306'
            )
            return connection
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None