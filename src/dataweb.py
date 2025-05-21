# dataweb.py
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class DataWeb:
    def __init__(self):
        self.url = "https://listado.mercadolibre.com.co/laptop#D[A:laptop]"

    def obtener_datos(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(self.url)

        try:
            # Espera explícita
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ui-search-result__wrapper"))
            )

            productos = driver.find_elements(By.CLASS_NAME, "ui-search-result__wrapper")
            print(f"📦 Productos encontrados: {len(productos)}")

            datos = []
            for producto in productos:
                try:
                    titulo = producto.find_element(By.TAG_NAME, "h2").text
                    precio = producto.find_element(By.CSS_SELECTOR, ".andes-money-amount__fraction").text
                    datos.append({
                        "titulo": titulo,
                        "precio": precio
                    })
                except Exception as e:
                    print("⚠️ Error al extraer producto:", e)
                    continue

            df = pd.DataFrame(datos)
            df = self.convertir_numericos(df)

            print("✅ Datos obtenidos y convertidos:")
            print(df.head())
            return df

        except Exception as err:
            print("❌ Error general en la extracción:", err)
            return pd.DataFrame()
        finally:
            driver.quit()

    def convertir_numericos(self, df=pd.DataFrame()):
        df = df.copy()
        if "precio" in df.columns:
            df["precio"] = (df["precio"]
                            .astype(str)
                            .str.replace(".", "", regex=False)
                            .str.replace(",", "", regex=False))
            df["precio"] = pd.to_numeric(df["precio"], errors="coerce")
        return df
