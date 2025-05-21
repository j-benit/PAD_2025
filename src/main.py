from dataweb import extraer_laptops
from database import DataBase
import pandas as pd

def main():
    try:
        datos = extraer_laptops()

        if not datos:
            print("No se extrajeron datos.")
            return

        df = pd.DataFrame(datos)
        print(df.head())

        # Guardar en CSV
        ruta_csv = "src/PAD_2025/src/static/csv/laptops.csv"
        df.to_csv(ruta_csv, index=False, encoding='utf-8')
        print(f"✅ CSV guardado en: {ruta_csv}")

        # Guardar en base de datos
        db = DataBase()
        db.guardar_df(df)

    except Exception as e:
        print("❌ Error al ejecutar extraer_laptops:")
        print(e)

if __name__ == "__main__":
    main()
