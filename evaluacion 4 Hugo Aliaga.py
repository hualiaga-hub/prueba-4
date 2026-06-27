# Lista principal de tareas
tareas=[]

#=======================
#FUNCIONES DE VALIDACION
#=======================

def validar_descripcion(descripcion):
    return descripcion.strip() != ""

def validar_prioridad(prioridad):
    return 1 <= prioridad <= 10

def validar_tiempo > 0
    return tiempo > 0

#================
#FUCION DEL MENU 
#================

def mostrar_menu():
    print("\n=====MENU PRINCIPAL=====")
    print("1.agregar tarea")
    print("2.buscar tarea")
    print("3.eliminar tarea")
    print("4.actualizar estado")
    print("5.mostrar tareas")
    print("6.salir")
    print("========================")

def leer_opcion()
    while True:
        try:
            opcion = int(input("seleccione una pcion (1-6): "))
            if 1 <= opcion <= 6:
                 return opcion
            else:
                print("Debe ingresar una opción entre 1 y 6.")
        except ValueError:
            print("Error: Ingrese un número válido.")

# ====================
# FUNCIONES DE TAREAS
# ====================

def agregar_tarea(lista):
    descripcion = input("Ingrese descripción: ")

    if not validar_descripcion(descripcion):
        print("Error: La descripción no puede estar vacía.")
        return

    try:
        prioridad = int(input("Ingrese prioridad (1-10): "))
        if not validar_prioridad(prioridad):
            print("Error: La prioridad debe estar entre 1 y 10.")
            return
    except ValueError:
        print("Error: La prioridad debe ser un número entero.")
        return

    try:
        tiempo = float(input("Ingrese tiempo estimado: "))
        if not validar_tiempo(tiempo):
            print("Error: El tiempo debe ser mayor que 0.")
            return
    except ValueError:
        print("Error: El tiempo debe ser un número.")
        return

    tarea = {
        "descripcion": descripcion,
        "prioridad": prioridad,
        "tiempo": tiempo,
        "completada": False
    }

    lista.append(tarea)
    print("Tarea registrada correctamente.")

def buscar_tarea(lista, descripcion):
    for i in range(len(lista)):
        if lista[i]["descripcion"] == descripcion:
            return i
    return -1

def eliminar_tarea(lista):
    descripcion = input("Ingrese descripción de la tarea a eliminar: ")

    posicion = buscar_tarea(lista, descripcion)

    if posicion != -1:
        lista.pop(posicion)
        print("Tarea eliminada correctamente.")
    else:
        print("La tarea no se encuentra registrada.")

def actualizar_estado(lista):
    for tarea in lista:
        if tarea["prioridad"] >= 5:
            tarea["completada"] = True
        else:
            tarea["completada"] = False

    print("Estado actualizado correctamente.")

def mostrar_tareas(lista):
    actualizar_estado(lista)

    if len(lista) == 0:
        print("No existen tareas registradas.")
        return

    print("\n=== LISTA DE TAREAS ===")

    for tarea in lista:
        estado = "COMPLETADA" if tarea["completada"] else "PENDIENTE"

        print(f"Descripción: {tarea['descripcion']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Tiempo estimado: {tarea['tiempo']}")
        print(f"Estado: {estado}")
        print("========================")

# ==================
# PROGRAMA PRINCIPAL
# ==================

while True:

    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_tarea(tareas)

    elif opcion == 2:
        descripcion = input("Ingrese descripción de la tarea a buscar: ")

        posicion = buscar_tarea(tareas, descripcion)

        if posicion != -1:
            tarea = tareas[posicion]

            print("\nTarea encontrada")
            print("Posición:", posicion)
            print("Descripción:", tarea["descripcion"])
            print("Prioridad:", tarea["prioridad"])
            print("Tiempo:", tarea["tiempo"])
            print("Completada:", tarea["completada"])
        else:
            print("Tarea no encontrada.")

    elif opcion == 3:
        eliminar_tarea(tareas)

    elif opcion == 4:
        actualizar_estado(tareas)

    elif opcion == 5:
        mostrar_tareas(tareas)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto.")
        break

