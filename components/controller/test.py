from connection import conn

if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM poblacion WHERE nombre like 'Esplugues%'")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
