# Un programa que determine si un número es positivo, negativo o cero.

numero = int(input("Ingrese un número entero: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")