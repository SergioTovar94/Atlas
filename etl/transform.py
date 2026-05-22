"""
Módulo de transformación de datos
"""
import pandas as pd

class Transformer:
    """
    Clase transformadora
    """
    def __init__(self):
        pass
    def transformar_clientes(self, df):
        """Transformaciones para tabla clientes"""
        df_transform = df.copy()
        df_transform['nombre'] = df_transform['nombre'].str.strip().str.encode('latin1').str.decode('utf-8')
        df_transform['ciudad'] = df_transform['ciudad'].str.strip().str.encode('latin1').str.decode('utf-8')
        # Validación de fechas
        df_transform['fecha_registro'] = pd.to_datetime(df_transform['fecha_registro'])
        print(f"Clientes transformados: {len(df_transform)} registros")
        return df_transform
    def transformar_productos(self, df):
        """Transformaciones para tabla productos"""
        df_transform = df.copy()
        # Limpiar nombres y categorías
        df_transform['nombre_producto'] = df_transform['nombre_producto'].str.strip().str.encode('latin1').str.decode('utf-8')
        df_transform['categoria'] = df_transform['categoria'].str.strip().str.encode('latin1').str.decode('utf-8')
        # Validar precios positivos
        df_transform['precio'] = df_transform['precio'].abs()
        print(f"Productos transformados: {len(df_transform)} registros")
        return df_transform
    def transformar_ventas(self, df_ventas):
        """Transformaciones para tabla ventas"""
        df_transform = df_ventas.copy()
        # Validar fechas
        df_transform['fecha_venta'] = pd.to_datetime(df_transform['fecha_venta'])
        # Validar unidades positivas
        df_transform['unidades'] = df_transform['unidades'].abs()
        print(f"Ventas transformadas: {len(df_transform)} registros")
        return df_transform
    def transformar_todos(self, datos_raw):
        """Aplica todas las transformaciones"""
        print("Iniciando transformaciones...")
        clientes_transform = self.transformar_clientes(datos_raw['clientes'])
        productos_transform = self.transformar_productos(datos_raw['productos'])
        ventas_transform = self.transformar_ventas(datos_raw['ventas'])
        print("Transformaciones completadas")
        return {
            'clientes': clientes_transform,
            'productos': productos_transform,
            'ventas': ventas_transform
        }
