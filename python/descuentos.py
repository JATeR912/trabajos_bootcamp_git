print ("¡Bienvenido a la tienda!")

descuento = 0
nombre = input("Ingrese nombre del cliente: ")
print("¡Bienvenido sr/sra", nombre,"!")
print()

# Descuento dia especial
semana = {
    1:"Lunes", 
    2:"Martes", 
    3:"Miercoles", 
    4:"Jueves", 
    5:"Viernes", 
    6:"Sabado", 
    7:"Domingo"
    }
print ("Codigo de dias de la semana")
for dias in semana:
    print (f"{dias}:{semana[dias]}")
dia_valido = False
while dia_valido == False:
    dia = input("ingrese el codigo del dia :")
    if dia == "1":
        print("¡Buen dia Lunes! ¡Has obtenido un descuento del 15% por ser dia lunes!")
        descuento += 15  
        dia_valido = True 
    elif dia == "2":
        print("¡Buen dia Martes! ¡Has obtenido un descuento del 15% por ser dia martes!")
        descuento += 15
        dia_valido = True
    elif dia == "3":
        print("¡Buen día Miércoles, Sr/Sra", nombre,"!")
        dia_valido = True
    elif dia == "4":
        print("¡Buen día Jueves, Sr/Sra", nombre,"!")
        dia_valido = True
    elif dia == "5":
        print("¡Buen día Viernes, Sr/Sra", nombre,"!")
        dia_valido = True
    elif dia == "6":
        print("¡Buen día Sábado, Sr/Sra", nombre,"!")
        dia_valido = True
    elif dia == "7":
        print("¡Buen día Domingo, Sr/Sra", nombre,"!")
        dia_valido = True
    else:
        print("Por favor ingrese un código de día válido.")
        dia_valido = False


#Descuento cliente frecuente
print()
cliente = input("¿Cliente frecuente? (si/no): ")
if cliente == "si":
    print("Gracias sr/sra", nombre, "por ser un cliente frecuente.")
    print("¡Has obtenido un descuento del 5%","en el total de su compra por ser cliente frecuente!")
    descuento += 5
else:
    print("Lo invitamos realizar más de cinco compras para obtener un descuento.")

#cantidad de productos y total compra
products = {
    1:"Pizza", 
    2:"Carne", 
    3:"Queso", 
    4:"Aceite de oliva", 
    5:"Café",
    6:"Helado",
    0:"Salir"
    }
valor = 0
total_compra = 0 
numero_productos = 0 
codigo = " "

while codigo != "0":
    print()
    print("Menu de productos:")
    for product in products:
        print (f"{product}:{products[product]}")
    codigo = input("Ingrese el código de producto: ")

    if codigo == "1":
        valor = 17
        print("Se seleccionó:", products[1])
        print("Valor del producto:", valor)
        cantidad = int(input("Ingrese cantidad de productos: "))
        print("Se añadió:", cantidad, "productos de", products[1], "al carrito.")
        numero_productos += cantidad
        total = valor * cantidad
        total_compra += total
    elif codigo == "2":
        valor = 30
        print("Se seleccionó:", products[2])
        print("Valor del producto:", valor)
        cantidad = int(input("Ingrese cantidad de productos: "))
        print("Se añadió:", cantidad, "productos de", products[2], "al carrito.")
        numero_productos += cantidad
        total = valor * cantidad
        total_compra += total
    elif codigo == "3":
        valor = 10
        print("Se seleccionó:", products[3])
        print("Valor del producto:", valor)
        cantidad = int(input("Ingrese cantidad de productos: "))
        print("Se añadió:", cantidad, "productos de", products[3], "al carrito.")
        numero_productos += cantidad
        total = valor * cantidad
        total_compra += total
    elif codigo == "4":
        valor = 25
        print("Se seleccionó:", products[4])
        print("Valor del producto:", valor)
        cantidad = int(input("Ingrese cantidad de productos: "))
        print("Se añadió:", cantidad, "productos de", products[4], "al carrito.")
        numero_productos += cantidad
        total = valor * cantidad
        total_compra += total
    elif codigo == "5":
        valor = 15
        print("Se seleccionó:", products[5])
        print("Valor del producto:", valor)
        cantidad = int(input("Ingrese cantidad de productos: "))
        print("Se añadió:", cantidad, "productos de", products[5], "al carrito.")
        numero_productos += cantidad
        total = valor * cantidad
        total_compra += total
    elif codigo == "6":
        valor = 8
        print("Se seleccionó:", products[6])
        print("Valor del producto:", valor)
        cantidad = int(input("Ingrese cantidad de productos: "))
        print("Se añadió:", cantidad, "productos de", products[6], "al carrito.")
        numero_productos += cantidad
        total = valor * cantidad
        total_compra += total
    elif codigo == "0":
        break
    else:
        print("Por favor ingrese un código de producto válido.")

print("Saliendo de la lista de productos...")

print()
print("Cantidad total de productos:", numero_productos)
print(f"Su compra asciende a un total de: $ {total_compra}")

if total_compra >= 500:
    descuento += 7
    print("Has obtenido un descuento del 7% por comprar mas de $500.")
else:
    descuento += 0

if numero_productos >= 10:
    descuento += 10
    print("Has obtenido un descuento del 10% por comprar mas de 10 productos.")
else:
    descuento += 0

print()
if descuento >= 30:
   descuento = 30
print("El descuento total es de", descuento, "%","en el total de su la compra.")

total_compra -= total_compra * descuento / 100
print("El total a pagar es de", total_compra)
print("Gracias por su compra, sr/sra ", nombre, ".")