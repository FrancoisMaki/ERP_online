import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def obtener_paises():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pais")
    data = cursor.fetchall()
    conn.close()
    return data

def insertar_pais(data):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO pais (paisid, iso3, nombre, nombre_ingles, codigo_numerico, prefijo_telefono, continente) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    valores = (
        data['paisid'], data['iso3'], data['nombre'], data['nombre_ingles'],
        data.get('codigo_numerico'), data.get('prefijo_telefono'), data.get('continente')
    )
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()
    return {"message": "País insertado"}
