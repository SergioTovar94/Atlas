USE prueba_ventas;
CREATE OR REPLACE VIEW vw_resumen_clientes AS
SELECT c.nombre AS cliente,
    c.ciudad,
    COUNT(v.id_venta) AS total_compras,
    MAX(v.fecha_venta) AS ultima_fecha_compra,
    COALESCE(SUM(v.unidades * p.precio), 0) AS total_gastado
FROM Clientes c
    LEFT JOIN Ventas v ON c.id_cliente = v.id_cliente
    LEFT JOIN Productos p ON v.id_producto = p.id_producto
GROUP BY c.id_cliente,
    c.nombre,
    c.ciudad;
SELECT *
FROM vw_resumen_clientes;