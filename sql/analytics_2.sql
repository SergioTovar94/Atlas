USE prueba_ventas;
SELECT c.nombre,
    c.ciudad,
    COUNT(v.id_venta) AS numero_compras,
    SUM(v.unidades * p.precio) AS total_gastado
FROM Clientes c
    INNER JOIN Ventas v ON c.id_cliente = v.id_cliente
    INNER JOIN Productos p ON v.id_producto = p.id_producto
WHERE v.fecha_venta >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY c.id_cliente,
    c.nombre,
    c.ciudad
ORDER BY total_gastado DESC
LIMIT 5;