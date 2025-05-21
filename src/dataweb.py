# dataweb.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


class DataWeb:
    def __init__(self):
        self.datos = []
        self.df = pd.DataFrame()

    def extraer_laptops(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        url = "https://listado.mercadolibre.com.co/laptop#D[A:laptop]"
        driver.get(url)
        time.sleep(5)

        productos = driver.find_elements(By.CLASS_NAME, "ui-search-result__wrapper")
        print(f"Productos encontrados: {len(productos)}")

        for producto in productos:
            try:
                titulo = producto.find_element(By.CSS_SELECTOR, ".ui-search-item__title").text
                precio = producto.find_element(By.CSS_SELECTOR, ".andes-money-amount__fraction").text
                self.datos.append({
                    "titulo": titulo,
                    "precio": precio
                })
            except Exception as e:
                print("Error al extraer producto:", e)
                continue

        driver.quit()
        self.df = pd.DataFrame(self.datos)

    def obtener_datos(self):
        return self.df

    def convertir_numericos(self, df):
        df = df.copy()
        if "precio" in df.columns:
            # Asegurarse de que 'precio' sea string antes de reemplazar
            df["precio"] = df["precio"].astype(str).str.replace(".", "", regex=False)
            df["precio"] = pd.to_numeric(df["precio"], errors="coerce")
        else:
            print("⚠️ La columna 'precio' no existe en el DataFrame. Columnas disponibles:", df.columns)
        return df
