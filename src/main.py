# main.py
from dataweb import extraer_laptops
from database import DataBase
import pandas as pd
import os

def main():
    datos = extraer_laptops()
    if not datos:
        print("⚠️ No se extrajeron datos.")
        return

    df = pd.DataFrame(datos)

    # Guardar CSV
    ruta_csv = "src/PAD_2025/src/static/csv/laptops.csv"
    os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)
    df.to_csv(ruta_csv, index=False, encoding="utf-8")
    print(f"✅ CSV guardado en: {ruta_csv}")

    # Guardar en base de datos
    db = DataBase()
    db.guardar_df(df)

if __name__ == "__main__":
    main()
