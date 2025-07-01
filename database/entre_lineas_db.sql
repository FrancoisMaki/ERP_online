--CREATE TABLE pais (
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
  provinciaid TINYINT UNSIGNED ZEROFILL NOT NULL,
  paisid CHAR(2) NOT NULL,
  FOREIGN KEY (provinciaid, paisid) REFERENCES provincia(provinciaid, paisid),
  FOREIGN KEY (paisid) REFERENCES pais(paisid),
  UNIQUE(nombre, provinciaid, paisid)
);

CREATE TABLE codigo_postal (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  paisid CHAR(2) NOT NULL,
  prefijo TINYINT UNSIGNED NOT NULL,     -- corregido
  resto VARCHAR(10) NOT NULL,
  poblacionid INT UNSIGNED NOT NULL,
  FOREIGN KEY (paisid) REFERENCES pais(paisid),
  FOREIGN KEY (prefijo, paisid) REFERENCES provincia(provinciaid, paisid),  -- clave compuesta
  FOREIGN KEY (poblacionid) REFERENCES poblacion(poblacionid),
  UNIQUE(paisid, prefijo, resto)
);


CREATE TABLE moneda (
    codigo CHAR(3) PRIMARY KEY,            -- Ej: EUR, USD
    nombre VARCHAR(50) NOT NULL,           -- Ej: Euro
    simbolo VARCHAR(10),                   -- Ej: €
    decimales TINYINT DEFAULT 2,           -- Ej: 2 para céntimos
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE tipo_cambio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    moneda_origen CHAR(3) NOT NULL,
    moneda_destino CHAR(3) NOT NULL,
    fecha DATE NOT NULL,
    tasa DECIMAL(12,6) NOT NULL,
    UNIQUE(moneda_origen, moneda_destino, fecha),
    FOREIGN KEY (moneda_origen) REFERENCES moneda(codigo),
    FOREIGN KEY (moneda_destino) REFERENCES moneda(codigo)
);

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    contraseña_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    rol ENUM('admin', 'empleado', 'cliente') DEFAULT 'empleado',
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE empresa (
    id_empresa INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cif VARCHAR(20) NOT NULL,
    direccion VARCHAR(100),
    poblacionid INT UNSIGNED,
    idioma VARCHAR(50),
    moneda CHAR(3),
    iva_general DECIMAL(5,2) DEFAULT 4.00,
    FOREIGN KEY (poblacionid) REFERENCES poblacion(poblacionid),
    FOREIGN KEY (moneda) REFERENCES moneda(codigo)
);

CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nif VARCHAR(20),
    direccion VARCHAR(100),
    poblacionid INT UNSIGNED,
    email VARCHAR(100),
    telefono VARCHAR(20),
    FOREIGN KEY (poblacionid) REFERENCES poblacion(poblacionid)
);

CREATE TABLE proveedor (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cif VARCHAR(20),
    direccion VARCHAR(100),
    poblacionid INT UNSIGNED,
    email VARCHAR(100),
    telefono VARCHAR(20),
    FOREIGN KEY (poblacionid) REFERENCES poblacion(poblacionid)
);

CREATE TABLE categoria (
  id_categoria INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL
);

CREATE TABLE autor (
  id_autor INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL
);

CREATE TABLE producto (
  isbn VARCHAR(20) NOT NULL PRIMARY KEY,
  titulo VARCHAR(200) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  stock INT DEFAULT 0,
  fecha_publicacion DATE,
  estado ENUM('nuevo', 'segunda_mano') DEFAULT 'nuevo',
  imagen_url TEXT
);

CREATE TABLE libro_autor (
  id_libro VARCHAR(20),
  id_autor INT,
  PRIMARY KEY (id_libro, id_autor),
  FOREIGN KEY (id_libro) REFERENCES producto(isbn),
  FOREIGN KEY (id_autor) REFERENCES autor(id_autor)
);

CREATE TABLE libro_categoria (
  id_libro VARCHAR(20),
  id_categoria INT,
  PRIMARY KEY (id_libro, id_categoria),
  FOREIGN KEY (id_libro) REFERENCES producto(isbn),
  FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

CREATE TABLE almacen (
  id_almacen INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  direccion VARCHAR(100),
  poblacionid INT UNSIGNED,
  FOREIGN KEY (poblacionid) REFERENCES poblacion(poblacionid)
);

CREATE TABLE movimiento_stock (
  id_movimiento INT AUTO_INCREMENT PRIMARY KEY,
  id_producto VARCHAR(20) NOT NULL,
  id_almacen INT NOT NULL,
  cantidad INT NOT NULL,
  tipo ENUM('entrada', 'salida') NOT NULL,
  fecha DATE NOT NULL,
  FOREIGN KEY (id_producto) REFERENCES producto(isbn),
  FOREIGN KEY (id_almacen) REFERENCES almacen(id_almacen)
);

CREATE TABLE cabfac (
  id_cabfac INT AUTO_INCREMENT PRIMARY KEY,
  id_cliente INT NOT NULL,
  fecha DATE NOT NULL,
  total DECIMAL(10,2),
  moneda CHAR(3),
  FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
  FOREIGN KEY (moneda) REFERENCES moneda(codigo)
);

CREATE TABLE linfac (
  id_linfac INT AUTO_INCREMENT PRIMARY KEY,
  id_cabfac INT,
  id_producto VARCHAR(20),
  cantidad INT NOT NULL,
  precio_unitario DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (id_cabfac) REFERENCES cabfac(id_cabfac),
  FOREIGN KEY (id_producto) REFERENCES producto(isbn)
);

CREATE TABLE cobropago (
  id_pago INT AUTO_INCREMENT PRIMARY KEY,
  id_cabfac INT,
  fecha_pago DATE,
  cantidad DECIMAL(10,2),
  metodo_pago VARCHAR(50),
  FOREIGN KEY (id_cabfac) REFERENCES cabfac(id_cabfac)
);

CREATE TABLE cabcompra (
  id_cabcompra INT AUTO_INCREMENT PRIMARY KEY,
  id_proveedor INT NOT NULL,
  fecha DATE NOT NULL,
  total DECIMAL(10,2),
  moneda CHAR(3),
  FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor),
  FOREIGN KEY (moneda) REFERENCES moneda(codigo)
);

CREATE TABLE lincompra (
  id_lincompra INT AUTO_INCREMENT PRIMARY KEY,
  id_cabcompra INT,
  id_producto VARCHAR(20),
  cantidad INT NOT NULL,
  precio_unitario DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (id_cabcompra) REFERENCES cabcompra(id_cabcompra),
  FOREIGN KEY (id_producto) REFERENCES producto(isbn)
);

CREATE TABLE pagocompra (
  id_pagocompra INT AUTO_INCREMENT PRIMARY KEY,
  id_cabcompra INT,
  fecha_pago DATE,
  cantidad DECIMAL(10,2),
  metodo_pago VARCHAR(50),
  FOREIGN KEY (id_cabcompra) REFERENCES cabcompra(id_cabcompra)
);





