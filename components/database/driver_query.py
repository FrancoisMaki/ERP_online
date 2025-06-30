import re

# Archivo entrada con las sentencias SQL antiguas
input_file = 'pbl_cod.txt'

# Archivo salida con las nuevas sentencias SQL
output_file = 'new_codipostal.sql'

# Cache para poblaciones ya procesadas y sus IDs asignados (simulados)
poblacion_cache = {}
next_poblacion_id = 1

def get_prefijo(cp, length=2):
    # Para España 2 dígitos para la provincia, puedes cambiar según país
    return cp[:length]

def get_resto(cp, length=2):
    return cp[length:]

def sanitize_value(val):
    if val is None or val.upper() == 'NULL':
        return None
    # Quitar comillas simples y demás para insertar limpio
    val = val.strip().strip("'")
    return val

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        line = line.strip()
        if not line:
            continue

        # Extraer valores con regex (simplificado para tu formato)
        m = re.search(r"VALUES\(([^)]+)\);", line, re.IGNORECASE)
        if not m:
            continue

        values_str = m.group(1)
        # Dividir respetando comas (considerando que no hay comas dentro de valores)
        parts = [v.strip() for v in values_str.split(',')]

        # Asumimos orden de columnas fijo según ejemplo:
        # internalid, cp, carrer, poblacio, provinciaid, provincia, paisid, pais

        internalid = int(parts[0])
        cp = sanitize_value(parts[1])
        carrer = sanitize_value(parts[2])
        poblacio = sanitize_value(parts[3])
        provinciaid = parts[4].strip("'")
        # provincia = sanitize_value(parts[5])  # no lo usamos
        paisid = parts[6].strip("'")
        # pais = sanitize_value(parts[7])  # no lo usamos

        # Si no existe en cache la población, la insertamos con nuevo id simulado
        if (poblacio, provinciaid, paisid) not in poblacion_cache:
            poblacion_id = next_poblacion_id
            poblacion_cache[(poblacio, provinciaid, paisid)] = poblacion_id
            next_poblacion_id += 1

            # Insert población
            f_out.write(f"INSERT INTO poblacion (poblacionid, nombre, provinciaid, paisid) VALUES ({poblacion_id}, '{poblacio}', '{provinciaid}', '{paisid}');\n")
        else:
            poblacion_id = poblacion_cache[(poblacio, provinciaid, paisid)]

        # Extraer prefijo y resto del cp
        prefijo = get_prefijo(cp)
        resto = get_resto(cp)

        # Insert código postal
        # Puedes adaptar la longitud del prefijo si en otros países es distinto
        f_out.write(f"INSERT INTO codigo_postal (paisid, prefijo, resto, poblacionid) VALUES ('{paisid}', '{prefijo}', '{resto}', {poblacion_id});\n")

        # Opcional: insertar calle o hacer tabla aparte si la quieres normalizar

print(f"Proceso finalizado. Nuevo archivo: {output_file}")
