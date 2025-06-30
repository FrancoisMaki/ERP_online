CREATE TABLE pais (
  paisid CHAR(2) NOT NULL PRIMARY KEY,        -- ISO alpha-2
  iso3 CHAR(3) NOT NULL UNIQUE,               -- ISO alpha-3
  nombre VARCHAR(100) NOT NULL,               -- Nombre local o traducido
  nombre_ingles VARCHAR(100) NOT NULL,        -- Nombre internacional
  codigo_numerico SMALLINT,                   -- ISO numeric (opcional)
  prefijo_telefono VARCHAR(10),               -- Ej: +34
  continente VARCHAR(30),                     -- Opcional
  activo BOOLEAN DEFAULT TRUE                 -- Por si quieres habilitar/deshabilitar
);

CREATE TABLE provincia (
  provinciaid TINYINT UNSIGNED ZEROFILL NOT NULL,  -- 01-52 para España
  nombre VARCHAR(100) NOT NULL,
  paisid CHAR(2) NOT NULL,
  codigo_iso VARCHAR(10),                          -- opcional: para provincias con código
  PRIMARY KEY (provinciaid, paisid),
  CONSTRAINT fk_provincia_pais FOREIGN KEY (paisid) REFERENCES pais(paisid)
)

CREATE TABLE poblacion (
  poblacionid INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  provinciaid CHAR(2) NOT NULL,
  paisid CHAR(2) NOT NULL,
  FOREIGN KEY (provinciaid) REFERENCES provincia(provinciaid),
  FOREIGN KEY (paisid) REFERENCES pais(paisid),
  UNIQUE(nombre, provinciaid, paisid) -- para evitar duplicados en la misma provincia y país
);

CREATE TABLE codigo_postal (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  paisid CHAR(2) NOT NULL,
  prefijo CHAR(2) NOT NULL,        -- los 2 primeros dígitos del CP que identifican la provincia
  resto VARCHAR(10) NOT NULL,      -- el resto del código postal que identifica la población/zona
  poblacionid INT UNSIGNED NOT NULL,
  FOREIGN KEY (paisid) REFERENCES pais(paisid),
  FOREIGN KEY (prefijo) REFERENCES provincia(provinciaid),
  FOREIGN KEY (poblacionid) REFERENCES poblacion(poblacionid),
  UNIQUE(paisid, prefijo, resto)   -- para evitar códigos postales duplicados
);





