menu = {1:"Agregar nueva tarea",
        2:"Todas las tareas",
        3:"Marcar tarea como completada",
        4:"Eliminar tarea",
        5:"Salir"        
}
tareas = []
def agregar():
    nueva_tarea = input("Ingrese la nueva tarea: ")
    tareas.append(nueva_tarea)
   # os.system(f'echo "{tarea}" >> tareas.txt')
    print ("tarea",nueva_tarea, "añadida a la lista.")

def mostrar():
    for tarea in tareas:
        print (tarea)

def tarea_completada():
    print (tareas)
    completada = str(input("Ingrese la tarea que desea marcar como completada: (si/no)"))
    if completada == "si":
        print ("Tarea completada")      
    elif completada == "no":
        print ("Tarea no completada")
    else:
        print ("Por favor ingrese si o no")
  

def eliminar():
    print (tareas)
    eliminar = input("Ingrese la tarea que desea eliminar: ")
    tareas.remove(eliminar)

print ("Bienvenido al gestor de tareas")
for opciones in menu:
    print(f"{opciones}: {menu[opciones]}")

seleccion = int(input("Seleccione una opcion: "))
while seleccion != 5:
    if seleccion == 1:
        agregar()
    elif seleccion == 2:
        print ("Todas las tareas:")
        mostrar()
    elif seleccion == 3:
        print ("Marcar tarea como completada:")
    elif seleccion == 4:
        print ("Eliminar tarea:")
        eliminar()
    elif seleccion == 5:
        print ("Salir")
    else:
        print ("Por favor ingrese una opcion valida")

    for opciones in menu:
        print(f"{opciones}: {menu[opciones]}")
    seleccion = int(input("Seleccione una opcion: "))

