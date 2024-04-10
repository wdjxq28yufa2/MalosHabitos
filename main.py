# main.py

def pedir_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    numero1 = pedir_numero("Ingrese el primer número: ")
    numero2 = pedir_numero("Ingrese el segundo número: ")

    print("Operaciones:")
    print("Suma:", numero1 + numero2)
    print("Resta:", numero1 - numero2)
    print("Multiplicación:", numero1 * numero2)

    if numero2 != 0:
        print("División:", numero1 / numero2)
    else:
        print("No se puede dividir por cero.")

if __name__ == "__main__":
    main()
