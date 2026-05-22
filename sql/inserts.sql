INSERT INTO Clientes (nombre, ciudad, fecha_registro)
VALUES ('Juan Pérez', 'Bogotá', '2023-01-15'),
    ('María López', 'Medellín', '2023-02-20'),
    ('Carlos Gómez', 'Cali', '2023-03-05'),
    ('Ana Torres', 'Bogotá', '2023-03-25'),
    ('Luis Ramírez', 'Barranquilla', '2023-04-10');
INSERT INTO Productos (nombre_producto, categoria, precio)
VALUES ('Smartphone XYZ', 'Electrónica', 500.00),
    ('Laptop Ultra', 'Electrónica', 1500.00),
    ('Juego de sábanas', 'Hogar', 200.00),
    ('Aspiradora', 'Hogar', 750.00),
    ('Camiseta Algodón', 'Ropa', 100.00);
INSERT INTO Ventas (id_cliente, id_producto, fecha_venta, unidades)
VALUES -- Juan Pérez compras
    (
        (
            SELECT id_cliente
            FROM Clientes
            WHERE nombre = 'Juan Pérez'
        ),
        (
            SELECT id_producto
            FROM Productos
            WHERE nombre_producto = 'Smartphone XYZ'
        ),
        '2023-05-01',
        2
    ),
    (
        (
            SELECT id_cliente
            FROM Clientes
            WHERE nombre = 'Juan Pérez'
        ),
        (
            SELECT id_producto
            FROM Productos
            WHERE nombre_producto = 'Juego de sábanas'
        ),
        '2023-05-15',
        1
    ),
    -- María López compras
    (
        (
            SELECT id_cliente
            FROM Clientes
            WHERE nombre = 'María López'
        ),
        (
            SELECT id_producto
            FROM Productos
            WHERE nombre_producto = 'Laptop Ultra'
        ),
        '2023-06-05',
        1
    ),
    -- Carlos Gómez compras
    (
        (
            SELECT id_cliente
            FROM Clientes
            WHERE nombre = 'Carlos Gómez'
        ),
        (
            SELECT id_producto
            FROM Productos
            WHERE nombre_producto = 'Aspiradora'
        ),
        '2023-06-20',
        3
    ),
    (
        (
            SELECT id_cliente
            FROM Clientes
            WHERE nombre = 'Carlos Gómez'
        ),
        (
            SELECT id_producto
            FROM Productos
            WHERE nombre_producto = 'Smartphone XYZ'
        ),
        '2023-06-25',
        1
    ),
    -- Ana Torres compras
    (
        (
            SELECT id_cliente
            FROM Clientes
            WHERE nombre = 'Ana Torres'
        ),
        (
            SELECT id_producto
            FROM Productos
            WHERE nombre_producto = 'Camiseta Algodón'
        ),
        '2023-07-10',
        4
    ),
    -- Luis Ramírez compras
    (
        (
            SELECT id_cliente
            FROM Clientes
            WHERE nombre = 'Luis Ramírez'
        ),
        (
            SELECT id_producto
            FROM Productos
            WHERE nombre_producto = 'Smartphone XYZ'
        ),
        '2023-07-15',
        2
    ),
    (
        (
            SELECT id_cliente
            FROM Clientes
            WHERE nombre = 'Luis Ramírez'
        ),
        (
            SELECT id_producto
            FROM Productos
            WHERE nombre_producto = 'Laptop Ultra'
        ),
        '2023-07-20',
        1
    );