import os
from components.controller.connection import conectar

# Leer - Obtener todos los países
def obtener_paises():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pais")
    data = cursor.fetchall()
    conn.close()
    return data

# Crear - Insertar un nuevo país
def insertar_pais(data):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = """INSERT INTO pais (
                    paisid, iso3, nombre, nombre_ingles, 
                    codigo_numerico, prefijo_telefono, continente
                ) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        valores = (
            data['paisid'], data['iso3'], data['nombre'], data['nombre_ingles'],
            data.get('codigo_numerico'), data.get('prefijo_telefono'), data.get('continente')
        )
        cursor.execute(sql, valores)
        conn.commit()
        conn.close()
        return {"message": "País insertado correctamente."}
    except Exception as e:
        return {"error": str(e)}

# Actualizar - Modificar un país por su ID
def actualizar_pais_en_db(paisid, data):
    try:
        conn = conectar()
        cursor = conn.cursor()
        campos = []
        valores = []

        # Solo actualizamos los campos que vienen en el JSON
        if 'nombre' in data:
            campos.append("nombre = %s")
            valores.append(data['nombre'])
        if 'nombre_ingles' in data:
            campos.append("nombre_ingles = %s")
            valores.append(data['nombre_ingles'])
        if 'iso3' in data:
            campos.append("iso3 = %s")
            valores.append(data['iso3'])
        if 'codigo_numerico' in data:
            campos.append("codigo_numerico = %s")
            valores.append(data['codigo_numerico'])
        if 'prefijo_telefono' in data:
            campos.append("prefijo_telefono = %s")
            valores.append(data['prefijo_telefono'])
        if 'continente' in data:
            campos.append("continente = %s")
            valores.append(data['continente'])

        if not campos:
            return {"error": "No se proporcionaron datos para actualizar."}

        sql = f"UPDATE pais SET {', '.join(campos)} WHERE paisid = %s"
        valores.append(paisid)

        cursor.execute(sql, tuple(valores))
        conn.commit()
        conn.close()
        return {"message": "País actualizado correctamente."}
    except Exception as e:
        return {"error": str(e)}

# Eliminar - Borrar un país por su ID
def eliminar_pais_de_db(paisid):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM pais WHERE paisid = %s"
        cursor.execute(sql, (paisid,))
        conn.commit()
        conn.close()
        return {"message": "País eliminado correctamente."}
    except Exception as e:
        return {"error": str(e)}
