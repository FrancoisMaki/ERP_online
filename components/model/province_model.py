import os 
from components.controller.connection import conectar

# Obtener todas las provincias
def obtener_provincias():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM provincia")
    provincias = cursor.fetchall()
    conn.close()
    return provincias

# Insertar una nueva provincia
def insertar_provincia(data):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = """INSERT INTO provincia (provinciaid, nombre, paisid, codigo_iso)
                 VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (
            data['provinciaid'],
            data['nombre'],
            data['paisid'],
            data.get('codigo_iso')
        ))
        conn.commit()
        conn.close()
        return {"message": "Provincia insertada correctamente."}
    except Exception as e:
        return {"error": str(e)}

# Actualizar provincia
def actualizar_provincia(provinciaid, paisid, data):
    try:
        conn = conectar()
        cursor = conn.cursor()
        campos = []
        valores = []

        if 'nombre' in data:
            campos.append("nombre = %s")
            valores.append(data['nombre'])
        if 'codigo_iso' in data:
            campos.append("codigo_iso = %s")
            valores.append(data['codigo_iso'])

        if not campos:
            return {"error": "No se proporcionaron datos para actualizar."}

        sql = f"UPDATE provincia SET {', '.join(campos)} WHERE provinciaid = %s AND paisid = %s"
        valores.extend([provinciaid, paisid])

        cursor.execute(sql, tuple(valores))
        conn.commit()
        conn.close()
        return {"message": "Provincia actualizada correctamente."}
    except Exception as e:
        return {"error": str(e)}

# Eliminar provincia
def eliminar_provincia(provinciaid, paisid):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM provincia WHERE provinciaid = %s AND paisid = %s", (provinciaid, paisid))
        conn.commit()
        conn.close()
        return {"message": "Provincia eliminada correctamente."}
    except Exception as e:
        return {"error": str(e)}
