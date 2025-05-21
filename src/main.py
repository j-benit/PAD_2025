from dataweb import DataWeb
import pandas as pd



def main():
    dataweb = DataWeb()
    df = dataweb.obtener_datos() 
    df = dataweb.convertir_numericos(df) # capa 2 
    df.to_csv("src/static/csv/data_extractor.csv", index=False)


if __name__ == "__main__":
    main()