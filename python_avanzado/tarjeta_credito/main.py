from credito import TarjetaCredito

if __name__ =="__main__":

    t1 = TarjetaCredito(0, 1000, 0.05)
    t2 = TarjetaCredito(0, 2000, 0.05)
    t3 = TarjetaCredito(0, 500, 0.05)

t1.compra(200).compra(300).pago(400).cobrar_interes().mostrar_info_tarjeta()
t2.compra(400).compra(100).compra(600).pago(300).pago(500).cobrar_interes().mostrar_info_tarjeta()
t3.compra(150).compra(150).compra(75).compra(125).compra(100).mostrar_info_tarjeta()

TarjetaCredito.mostrar_todo_tarjetas()