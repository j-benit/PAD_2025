from dataweb import extraer_laptops

def main():
    laptops = extraer_laptops()
    for laptop in laptops:
        print(f"Título: {laptop['titulo']}")
        print(f"Precio: ${laptop['precio']}")
        print("-" * 30)

if __name__ == "__main__":
    main()