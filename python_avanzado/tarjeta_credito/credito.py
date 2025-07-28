class TarjetaCredito:

   #Incluye en este método valores por default
    tarjetas_creadas = []  
    def __init__(self, saldo_pagar, limite_credito, intereses):
         self.saldo_pagar = saldo_pagar
         self.limite_credito = limite_credito
         self.intereses = intereses
         TarjetaCredito.tarjetas_creadas.append(self)
       #TU CODIGO (Aquí va los atributos de instancia y sus asignaciones de valor)

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito: 
            self.saldo_pagar += monto
            print(f"Compra realizada por un monto de ${monto}. Cupo de credito utilizado: ${self.saldo_pagar}.")
        else:
            print(f"Tarjeta Rechazada, has alcanzado tu límite de crédito.")  
        return self
       #TU CODIGO: aumenta el saldo_pagar de acuerdo al monto recibido siempre y cuando la tarjeta de crédito no haya llegado 
       # a su límite crediticio. De lo contrario, que imprima: “Tarjeta Rechazada, has alcanzado tu límite de crédito”.

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self
       #TU CODIGO: disminuye el saldo_pagar de la tarjeta.

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        print(f"Límite de Crédito: ${self.limite_credito}")
        print(f"Intereses: {self.intereses}")
        return self
       #TU CODIGO: imprime en la consola el saldo a pagar de la tarjeta. Por ejemplo: “Saldo a Pagar: $100”

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        print(f"Intereses cobrados. Nuevo saldo a pagar: ${self.saldo_pagar}")
        return self
       #TU CODIGO: aumenta el saldo_pagar cobrando intereses. Es decir al saldo_pagar actual se le agregará el saldo_pagar * los intereses.

    @classmethod
    def mostrar_todo_tarjetas(cls):
        for tarjeta in cls.tarjetas_creadas:
            tarjeta.mostrar_info_tarjeta()
        return
   #BONUS: crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas. En el capítulo pasado te dimos algunas pistas de cómo realizarlo.