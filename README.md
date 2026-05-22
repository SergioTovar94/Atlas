# Prueba Técnica - Ingeniero de Desarrollo de Software

## Descripción

Prueba que evalúa habilidades en SQL, ETL, API, Dashboard y Git.

## Objetivos

### A. Bases de datos

1. Se construye una base de datos en MySQL con tres tablas: clientes, productos y ventas.

**Deciciones de negocio**

- Agregar campo de nombre de producto en tabla productos.

**Decisiones técnicas:**

- Uso de docker para el despliegue de MySQL.
- Uso de .env para definición de variables de entorno.
- .env no expuesto en gitignore para efectos de la prueba.
- Carpeta de scripts sql para creación de base de datos, creación de tablas e insersión.
- Inserciones de ventas a partir de subconsultas para obtener independencia de los Ids asignados e inserciones portables.
  Decisión tomada teniendo en cuenta:
  - Poca cantidad de insersiones - no es muy costosa computacionalmente.
  - Luego de la adición del campo nombre de producto, no habrá conflictos.

2. Se realizan 3 consultas que incluyen JOINS, Vistas y otras sentencias.

### B. ETL

1. Conexión a base de datos de Sección A.
2. Extraer información de las tablas y cargar en otra base de datos. Esta será SQLite para que no deba requerirse otro servidor.

### C. API

1. API con Python que tiene endpoint que devuelve JSON de total de ventas por categoría.

### D. Power BI

1. Gráfico de ventas por categoría.
2. Gráfico de categorías por mes.
3. Cliente que más compra.

### E. Git

1. En todo el proceso de desarrollo se usará git.
2. Se irán adjuntando los entregables (Base de datos, ETL, API, Dasboard).

## Estructura del proyecto

(Se irá completando durante el desarrollo)

## Requisitos

(Se irá completando durante el desarrollo)

## Instalación

1. Ejecutar el contenedor

```
docker-compose up -d
```

2. Verificar que el contenedor fue creado

```
docker ps
```

3. Copiar los archivos SQL al contenedor

```
docker cp sql/create.sql prueba_mysql:/create.sql
```

```
docker cp sql/tables.sql prueba_mysql:/tables.sql
```

```
docker cp sql/inserts.sql prueba_mysql:/inserts.sql
```

## Creación de base de datos, tablas e inserción de datos

4. Entrar al contenedor de MySQL

```
docker exec -it prueba_mysql bash
```

5. Conectarse a MySQL

```
mysql -uroot -proot123
```

6. Ejecutar los scripts

```
source /create_db.sql;
```

```
source /tables.sql;
```

```
source /inserts.sql;
```

7. Verificar que todo está correcto

```
USE prueba_ventas;
SHOW TABLES;
SELECT COUNT(*) FROM Clientes;
SELECT COUNT(*) FROM Productos;
SELECT COUNT(*) FROM Ventas;
```

## Ejercios

1. Copiar los ejecicios al contenedor

```
docker cp sql/analytics_1.sql prueba_mysql:/analytics_1.sql
docker cp sql/analytics_2.sql prueba_mysql:/analytics_2.sql
docker cp sql/analytics_3.sql prueba_mysql:/analytics_3.sql
```

2. Entrar al contenedor, a la base de datos y ejecutar los scripts

```
docker exec -it prueba_mysql bash
mysql -uroot -proot123
source /analytics_1.sql
source /analytics_2.sql
source /analytics_3.sql
```

## Estado del proyecto

En construcción
