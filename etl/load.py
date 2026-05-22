"""
Módulo de carga de datos
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
import yaml

class Loader:
    """
    Clase de carga de datos
    """
    def __init__(self, config_path='etl/config/config.yaml'):
        with open(config_path, 'r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file)
        destino = self.config['destino']
        self.engine = create_engine(f"sqlite:///{destino['ruta']}?charset=utf8")
    def cargar_tabla(self, df, nombre_tabla, if_exists='replace'):
        """Carga un DataFrame a la tabla destino"""
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.encode('utf-8', errors='ignore').str.decode('utf-8')
        df.to_sql(nombre_tabla, self.engine, if_exists=if_exists, index=False)
        print(f"Cargados {len(df)} registros en {nombre_tabla}")
        return True
    def cargar_todos(self, datos_transformados):
        """Carga todas las tablas transformadas"""
        print("Iniciando carga...")
        resultados = {}
        for nombre_tabla, df in datos_transformados.items():
            exito = self.cargar_tabla(df, nombre_tabla, if_exists='replace')
            resultados[nombre_tabla] = exito
        print("Carga completada")
        return resultados
