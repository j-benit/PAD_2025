from dataweb import extraer_laptops

def main():
    try:
        extraer_laptops()
    except Exception as e:
        print("❌ Error al ejecutar extraer_laptops:")
        print(e)

if __name__ == "__main__":
    main()
