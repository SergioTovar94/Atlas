"""
API sencilla
"""
from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/ventas-por-categoria")
def ventas_por_categoria():
    """
    Método de ventas por categoría
    """
    # Conectar a SQLite
    conn = sqlite3.connect('data/destino/warehouse.db')
    cursor = conn.cursor()
    # Consultar ventas por categoría
    cursor.execute("""
        SELECT 
            p.categoria,
            SUM(v.unidades) as total_unidades,
            SUM(v.unidades * p.precio) as total_ventas
        FROM Ventas v
        JOIN Productos p ON v.id_producto = p.id_producto
        GROUP BY p.categoria
    """)
    # Obtener resultados
    resultados = cursor.fetchall()
    conn.close()
    # Convertir a JSON
    datos = []
    for categoria, unidades, ventas in resultados:
        datos.append({
            "categoria": categoria,
            "total_unidades": unidades,
            "total_ventas": float(ventas)
        })
    return {"ventas_por_categoria": datos}
