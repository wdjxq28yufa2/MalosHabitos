# ejemplo1.py

import library

def main():
    while True:
        try:
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    resultado = library.suma(x, y)
    print("La suma de los números es:", resultado)

if __name__ == "__main__":
    main()
