"""
Módulo de extracción de datos
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sqlalchemy import create_engine
import yaml

class Extractor:
    """
    Clase extractora
    """
    def __init__(self, config_path='etl/config/config.yaml'):
        with open(config_path, 'r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file)
        origen = self.config['origen']
        self.engine = create_engine(
            f"mysql+pymysql://{origen['usuario']}:{origen['password']}@"
            f"{origen['host']}:{origen['puerto']}/{origen['database']}"
        )
    def extraer_tabla(self, nombre_tabla):
        """Extrae una tabla completa de MySQL"""
        query = f"SELECT * FROM {nombre_tabla}"
        df = pd.read_sql(query, self.engine)
        print(f" Extraídos {len(df)} registros de {nombre_tabla}")
        return df
    def extraer_todas(self):
        """Extrae las 3 tablas: Clientes, Productos, Ventas"""
        print("Iniciando extracción...")
        datos = {
            'clientes': self.extraer_tabla('Clientes'),
            'productos': self.extraer_tabla('Productos'),
            'ventas': self.extraer_tabla('Ventas')
        }
        print("Extracción completada")
        return datos

if __name__ == "__main__":
    extractor = Extractor()
    data = extractor.extraer_todas()
    for nombre, dataframe  in data.items():
        print(f"\n{nombre}:")
        print(dataframe .head())
