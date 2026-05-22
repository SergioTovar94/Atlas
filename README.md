# Prueba Técnica - Ingeniero de Desarrollo de Software

## Descripción

Prueba que evalúa habilidades en SQL, ETL, API, Dashboard y Git.

## Objetivos

### A. Bases de datos

1. Se construye una base de datos en MySQL con tres tablas: clientes, productos y ventas.

**Deciciones de negocio**

- Agregar campo de nombre de producto en tabla productos.

**Decisiones técnicas:**

- Uso de Docker para el despliegue de MySQL.
- Uso de `.env` para definición de variables de entorno.
- `.env` no expuesto en `.gitignore` solo para efectos de la prueba (en entorno real debe estar ignorado).
- Carpeta `sql/` con scripts organizados:
  - `create_db.sql` - creación de la base de datos
  - `tables.sql` - creación de tablas
  - `inserts.sql` - inserción de datos
  - `analytics_1.sql`, `analytics_2.sql`, `analytics_3.sql` - consultas requeridas
- Inserciones de ventas realizadas mediante **subconsultas** para independencia de los IDs asignados e inserciones portables.
  - Decisión tomada considerando:
    - Poca cantidad de inserciones → no es costoso computacionalmente.
    - Luego de la adición del campo `nombre_producto`, no hay conflictos.

2. Se realizan 3 consultas que incluyen JOINS, Vistas y otras sentencias.

### B. ETL

1. Conexión a base de datos MySQL (origen).
2. Extracción de información de las tablas y carga en otra base de datos (destino).
3. Base de datos destino: **SQLite** (no requiere servidor adicional).
4. Transformaciones aplicadas: limpieza de espacios, validación de fechas, precios positivos.

### C. API

1. API con Python (FastAPI) que tiene un endpoint que devuelve JSON con el total de ventas por categoría.
2. Endpoint: `GET /ventas-por-categoria`

### D. Power BI

1. Gráfico de ventas por categoría.
2. Gráfico de categorías por mes (línea temporal).
3. Cliente que más compra (Top 1).

### E. Git

1. En todo el proceso de desarrollo se usa Git.
2. Commits atómicos por cada funcionalidad.
3. Se adjuntan todos los entregables en el repositorio.

## Estructura del proyecto

atlas/
├── .env # Variables de entorno (credenciales MySQL)
├── .gitignore # Archivos ignorados por Git
├── README.md # Este archivo
├── docker-compose.yml # Configuración del contenedor MySQL
├── requirements.txt # Dependencias Python
│
├── sql/ # Scripts SQL
│ ├── create_db.sql # CREATE DATABASE
│ ├── tables.sql # CREATE TABLE
│ ├── inserts.sql # INSERT de datos
│ ├── analytics_1.sql # Ventas totales por mes y categoría
│ ├── analytics_2.sql # TOP 5 clientes último año
│ └── analytics_3.sql # Vista resumen clientes
│
├── etl/ # Pipeline ETL
│ ├── extract.py # Extracción desde MySQL
│ ├── transform.py # Transformaciones
│ ├── load.py # Carga a SQLite
│ ├── run_etl.py # Orquestador
│ └── config/
│ └── config.yaml # Configuración de conexiones
│
├── api/ # API FastAPI
│ └── main.py # Endpoint /ventas-por-categoria
│
├── dashboard/ # Power BI
│ └── ventas_dashboard.pbix # Dashboard con 3 visuales
│
└── data/ # Datos generados (ignorados por Git)
└── destino/
└── warehouse.db # Base SQLite destino del ETL

## Requisitos

- Docker y Docker Compose
- Python 3.9+
- Power BI Desktop (para visualizar dashboard)
- Git

## Instalación y ejecución

1. Clonar el repositorio

```bash
git clone <url-del-repo>
cd atlas
```

2. Configurar variables de entorno
   Crear archivo .env en la raíz:

```bash
env
MYSQL_ROOT_PASSWORD=root123
```

3. Ejecutar el contenedor

```bash
docker-compose up -d
```

4. Verificar que el contenedor fue creado

```bash
docker ps
```

## Creación de base de datos, tablas e inserción de datos

5. Entrar al contenedor de MySQL

```
docker exec -it prueba_mysql bash
```

6. Conectarse a MySQL

```
mysql -uroot -proot123
```

7. Ejecutar los scripts

```
source /create_db.sql;
```

```
source /tables.sql;
```

```
source /inserts.sql;
```

8. Verificar que todo está correcto

```
USE prueba_ventas;
SHOW TABLES;
SELECT COUNT(*) FROM Clientes;
SELECT COUNT(*) FROM Productos;
SELECT COUNT(*) FROM Ventas;
```

## Ejercios

1. Entrar al contenedor, a la base de datos y ejecutar los scripts

```
docker exec -it prueba_mysql bash
mysql -uroot -proot123
source /analytics_1.sql
source /analytics_2.sql
source /analytics_3.sql
```

2. Ejecutar el ETL (Sección B)

```bash
# Crear entorno virtual
python -m venv venv
# Activarlo
venv\Scripts\activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Ejecutar ETL

```bash
python etl/run_etl.py
```

3. Ejecutar la API (Sección C)

```bash
uvicorn api.main:app --reload --port 8000
```

Probar en navegador: http://localhost:8000/ventas-por-categoria

4. Abrir Dashboard Power BI (Sección D)

- Abrir Power BI Desktop
- Abrir archivo dashboard/ventas_dashboard.pbix
- Conectar a MySQL (servidor: localhost, base: prueba_ventas, usuario: root, contraseña: root123)
- Visualizar los 3 gráficos
