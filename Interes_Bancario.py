# cuenta_bancaria.py

class CuentaBancaria:
    def __init__(self, saldo_inicial: float):
        """Inicializa la cuenta bancaria con un saldo."""
        self.saldo = saldo_inicial

    def calcular_interes_anual(self):
        """Calcula el interés anual basado en el saldo de la cuenta."""
        if self.saldo < 10000:
            self.saldo *= 1.03  # 3% de interés
        else:
            self.saldo *= 1.04  # 4% de interés

    def mostrar_saldo_final(self):
        """Muestra el saldo final de la cuenta después de un año."""
        print(f"El saldo final después de un año es: ${self.saldo:.2f}")
