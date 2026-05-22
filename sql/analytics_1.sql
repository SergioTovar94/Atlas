USE prueba_ventas;
SELECT DATE_FORMAT(v.fecha_venta, '%Y-%m') AS mes,
    p.categoria,
    SUM(v.unidades * p.precio) AS total_ventas_monetarias
FROM Ventas v
    JOIN Productos p
WHERE v.id_producto = p.id_producto
GROUP BY DATE_FORMAT(v.fecha_venta, '%Y-%m'),
    p.categoria;