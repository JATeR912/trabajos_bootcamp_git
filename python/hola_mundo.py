# 1. Imprimir "Hola, mundo"
print("Hola, mundo")

# 2. Imprimir "Hola, nombre" con una variable
nombre = "Johana"
print("Hola," , nombre ) # con coma
print("Hola, " + nombre) # con signo +

# 3. Imprimir "Hola número!" con el número en una variable
numero = 219
print("Hola" , numero,"!") # con coma
# print("Hola" + numero + "!") # con signo + - con error
print("Hola " + str(numero) +"!") # con signo + - sin error

# 4. Imprimir "¡Me encanta comer ramen y ensaladas!" con las comidas en variables
comida1 = "ramen"
comida2 = "ensaladas"
print("¡Me encanta comer {} y {}!".format(comida1, comida2)) # con .format()
print(f"!Me encanta comer {comida1} y {comida2}!") # con una cadena f

# EXTRA Imprimir usando %-formating 
print("Hola, me llamo %s y mi número favorito es %d." % (nombre, numero))

# EXTRA Imprimir directamente usando .upper() y .lower()
print("Mi nombre es Johana.".upper())
print("Mi nombre es Johana.".lower())