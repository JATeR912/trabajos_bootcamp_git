#Cambia el valor 3 en matriz por 6.
matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz [1][0] = 6
print (matriz)

#Cambia el nombre del primer cantante por "Enrique Martin Morales".
cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"
print (cantantes)

#En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".
ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"
print (ciudades)

#En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.
coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431
print (coordenadas)

# Recorrer una lista de diccionarios:  Utiliza estructuras de control para iterar la lista cantantes. Muestra el nombre y país de cada cantante.
cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
for cantante in cantantes:
    print (cantante["nombre"], cantante["pais"])

#* BONUS: Presenta cada entrada con el siguiente formato: nombre - [Nombre del cantante], pais - [País]
for cantante in cantantes:
    print (f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")

#Obtener valores específicos desde una lista de diccionarios:  Utilizando la lista cantantes, imprime por separado todos los valores correspondientes a la clave "nombre".
cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
for  info in cantantes:
    print(info["nombre"])
# Luego, imprime todos los valores correspondientes a la clave "pais".
for  info in cantantes:
    print(info["pais"])

#Recorrer un diccionario con listas como valores:
costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
#Imprimir la cantidad de elementos en cada lista seguida del nombre de la clave en mayúsculas.
for details in costa_rica:
    print (len(costa_rica[details]), details.upper())

#Imprimir Cada elemento de la lista correspondiente, en líneas separadas.
for detail in costa_rica.values():
    for item in detail:
        print (item) 