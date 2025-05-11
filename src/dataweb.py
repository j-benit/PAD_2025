from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar opciones de Chrome para el modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializar el driver de Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL de búsqueda de laptops
url = "https://listado.mercadolibre.com.co/laptop#D[A:laptop]"
driver.get(url)
time.sleep(5)  # Esperar a que la página cargue

# Extraer los productos
productos = driver.find_elements(By.CLASS_NAME, "ui-search-result__wrapper")

print(f"Productos encontrados: {len(productos)}")

for producto in productos:
    try:
        # Intentar encontrar el título y el precio con selectores más generales
        titulo = producto.find_element(By.CSS_SELECTOR, "h2, .ui-search-item__title").text
        precio = producto.find_element(By.CSS_SELECTOR, ".andes-money-amount__fraction").text
        print(f"Título: {titulo}")
        print(f"Precio: ${precio}")
        print("-" * 10)
    except Exception as e:
        print("Error al extraer producto:", e)
        continue

# Opcional: Imprimir detalles de un producto específico
if productos:
    p = productos[0]  # El primer producto
    print("Primer producto:", p.text)

# Cerrar el navegador
driver.quit()
