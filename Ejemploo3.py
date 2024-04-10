# ejemplo3.py

import library

def main():
    while True:
        try:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la base y la altura.")

    area_rectangulo = library.calcular_area_rectangulo(base, altura)
    print("Área del rectángulo:", area_rectangulo)

    while True:
        try:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la base y la altura del triángulo.")

    area_triangulo = library.calcular_area_triangulo(base, altura)
    print("Área del triángulo:", area_triangulo)

if __name__ == "__main__":
    main()
