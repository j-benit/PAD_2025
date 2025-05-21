# database.py
import pandas as pd
import sqlite3
import os

class DataBase:
    def __init__(self):
        # Asegúrate de que la ruta exista
        os.makedirs("src/PAD_2025/src/static/db", exist_ok=True)
        self.rutadb = "src/PAD_2025/src/static/db/laptops.sqlite"

    def guardar_df(self, df=pd.DataFrame()):
        try:
            conn = sqlite3.connect(self.rutadb)
            df["fecha_create"] = pd.Timestamp.now()
            df["fecha_update"] = pd.Timestamp.now()
            df.to_sql("laptops_analisis", conn, if_exists='replace', index=False)
            print("✅ Datos guardados en base de datos.")
        except Exception as e:
            print(f"Error al guardar en la base de datos: {e}")

    def obtener_datos(self, nombre_tabla="laptops_analisis"):
        try:
            conn = sqlite3.connect(self.rutadb)
            df = pd.read_sql_query(f"SELECT * FROM {nombre_tabla}", conn)
            print(f" Registros recuperados: {df.shape[0]}")
            return df
        except Exception as e:
            print(f"❌ Error al leer la base de datos: {e}")
            return pd.DataFrame()
