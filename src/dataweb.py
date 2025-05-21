import pandas as pd
import requests
from bs4 import BeautifulSoup

class DataWebML:
    def __init__(self):
        self.url = "https://listado.mercadolibre.com.co/laptop#D[A:laptop]"

    def obtener_datos(self):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0"
            }
            respuesta = requests.get(self.url, headers=headers)
            if respuesta.status_code != 200:
                print("Error al acceder a la página")
                return pd.DataFrame()

            soup = BeautifulSoup(respuesta.text, 'html.parser')

            titulos = soup.select(".ui-search-item__title")
            precios = soup.select(".andes-money-amount__fraction")

            productos = []
            for titulo, precio in zip(titulos, precios):
                productos.append({
                    "titulo": titulo.get_text(strip=True),
                    "precio": precio.get_text(strip=True)
                })

            df = pd.DataFrame(productos)
            print("Datos extraídos:")
            print(df.head())
            return df

        except Exception as e:
            print
