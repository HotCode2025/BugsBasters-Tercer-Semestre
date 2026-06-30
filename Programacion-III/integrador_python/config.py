import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Esto carga el .env
load_dotenv() 
DB_URL = os.getenv("DATABASE_URL")

class DatabaseConfig:
    @staticmethod
    def get_connection():
        try:
            # Opción rápida: Cambia los valores aquí directamente
            connection = mysql.connector.connect(
                host='localhost',
                database='clinica_db',  # Asegúrate que el nombre coincida con tu BD
                user='root',
                password='44282458s',   # Tu contraseña real
                port='3306'
            )
            return connection
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None