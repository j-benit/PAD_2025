from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

class DataWeb:
    def __init__(self):
        self.url = "https://listado.mercadolibre.com.co/laptop#D[A:laptop]"

    def obtener_datos(self):
        opciones = Options()
        opciones.add_argument("--headless")
        opciones.add_argument("--no-sandbox")
        opciones.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opciones)
        driver.get(self.url)
        time.sleep(5)  # Espera para que cargue el JS

        productos = driver.find_elements(By.CLASS_NAME, "ui-search-result__wrapper")

        datos = []
        for producto in productos:
            try:
                titulo = producto.find_element(By.CSS_SELECTOR, ".ui-search-item__title").text
                precio = producto.find_element(By.CSS_SELECTOR, ".andes-money-amount__fraction").text
                datos.append({
                    "titulo": titulo,
                    "precio": precio
                })
            except Exception as e:
                print(f"Error al extraer producto: {e}")
                continue

        driver.quit()
        df = pd.DataFrame(datos)
        return df

# Ejemplo de uso:
# dw = DataWebML()
# df = dw.obtener_datos()
# print(df.head())
