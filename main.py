# main.py

from Interes_Bancario import CuentaBancaria

def main():
    # Solicitar el saldo inicial al usuario
    saldo_inicial = float(input("Introduce el saldo inicial: "))

    # Crear una instancia de CuentaBancaria con el saldo inicial
    cuenta = CuentaBancaria(saldo_inicial)

    # Calcular el interés anual
    cuenta.calcular_interes_anual()

    # Mostrar el saldo final
    cuenta.mostrar_saldo_final()

if __name__ == "__main__":
    main()
