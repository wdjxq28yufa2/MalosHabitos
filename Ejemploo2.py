# ejemplo2.py

import library

def main():
    while True:
        try:
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            z = float(input("Ingrese el tercer número: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    resultado_multiplicacion = library.multiplicar(x, y)
    resultado_final = library.suma(resultado_multiplicacion, z)
    print("El resultado es:", resultado_final)

if __name__ == "__main__":
    main()
