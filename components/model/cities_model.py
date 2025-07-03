from components.controller.connection import conn

# Obtener todas las poblaciones
def obtener_poblaciones():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM poblacion")
    poblaciones = cursor.fetchall()
    conn.close()
    return poblaciones

# Insertar nueva población
def insertar_poblacion(data):
    try:
        cursor = conn.cursor()
        sql = """INSERT INTO poblacion (nombre, provinciaid, paisid)
                 VALUES (%s, %s, %s)"""
        cursor.execute(sql, (
            data['nombre'],
            data['provinciaid'],
            data['paisid']
        ))
        conn.commit()
        conn.close()
        return {"message": "Población insertada correctamente."}
    except Exception as e:
        return {"error": str(e)}

# Actualizar población
def actualizar_poblacion(poblacionid, data):
    try:
        cursor = conn.cursor()
        campos = []
        valores = []

        if 'nombre' in data:
            campos.append("nombre = %s")
            valores.append(data['nombre'])
        if 'provinciaid' in data:
            campos.append("provinciaid = %s")
            valores.append(data['provinciaid'])
        if 'paisid' in data:
            campos.append("paisid = %s")
            valores.append(data['paisid'])

        if not campos:
            return {"error": "No se proporcionaron datos para actualizar."}

        sql = f"UPDATE poblacion SET {', '.join(campos)} WHERE poblacionid = %s"
        valores.append(poblacionid)

        cursor.execute(sql, tuple(valores))
        conn.commit()
        conn.close()
        return {"message": "Población actualizada correctamente."}
    except Exception as e:
        return {"error": str(e)}

# Eliminar población
def eliminar_poblacion(poblacionid):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM poblacion WHERE poblacionid = %s", (poblacionid,))
        conn.commit()
        conn.close()
        return {"message": "Población eliminada correctamente."}
    except Exception as e:
        return {"error": str(e)}
