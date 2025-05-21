from dataweb import DataWeb
from database import DataBase
import pandas as pd


def main():
    dataweb = DataWeb()
    dataweb.extraer_laptops()
    df = dataweb.obtener_datos()
    df = dataweb.convertir_numericos(df)

    df.to_csv("src/static/csv/data_extractor.csv", index=False)

    database = DataBase()
    df_db = pd.read_csv("src/static/csv/data_extractor.csv")
    database.guardar_df(df_db)

    df_db2 = database.obtener_datos()
    df_db2.to_csv("src/static/csv/data_db.csv", index=False)


if __name__ == "__main__":
    main_1()
