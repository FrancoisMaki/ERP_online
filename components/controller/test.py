from connection import conn

if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pais")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()
