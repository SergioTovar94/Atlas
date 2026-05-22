"""
Modulo orquestador
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extract import Extractor
from transform import Transformer
from load import Loader

def run_etl():
    """Método orquestador"""
    print("Iniciando ETL")
    # 1. Extracción
    print("\nPaso 1/3: Extrayendo datos...")
    extractor = Extractor()
    datos_raw = extractor.extraer_todas()
    # 2. Transformación (usando tu módulo)
    print("\nPaso 2/3: Transformando datos...")
    transformer = Transformer()
    datos_transformados = transformer.transformar_todos(datos_raw)
    # 3. Carga
    print("\nPaso 3/3: Cargando datos...")
    loader = Loader()
    loader.cargar_todos(datos_transformados)
    print("\nETL completado")

if __name__ == "__main__":
    run_etl()
