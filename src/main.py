# main.py
from dataweb import DataWeb
from database import DataBase
import pandas as pd

def main():
    dataweb = DataWeb()
    df = dataweb.obtener_datos()

    if df.empty:
        print(" No se extrajeron datos.")
        return

    df.to_csv("src/static/csv/data_extractor.csv", index=False)

    database = DataBase()
    database.guardar_df(df)

    df_db = database.obtener_datos()
    df_db.to_csv("src/static/csv/data_db.csv", index=False)
    print(" Proceso completado correctamente.")

if __name__ == "__main__":
    main()
