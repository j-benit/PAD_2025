from dataweb import extraer_laptops
from database import DataBase
import pandas as pd


def main_1():
    dataweb = extraer_laptops()
    df = dataweb.obtener_datos() 
    df = dataweb.convertir_numericos(df) # capa 2 
    df.to_csv("src/edu_pad/static/csv/data_extractor.csv", index=False)

    database = DataBase()
    df = pd.read_csv("src/edu_pad/static/csv/data_extractor.csv")
    df_db = database.guardar_df(df)
    df_db2 = database.obtener_datos() # capa 3 guardar 
    df_db2.to_csv("src/edu_pad/static/csv/data_db.csv", index=False)




if __name__ == "__main__":
    main_1()