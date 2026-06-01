# Recibe una tarea determinada, la almacena y se puede marcar como hecha, pendiente
from pathlib import Path
import json

def CARGAR_DATOS_JSON(ruta):
    try:
        with open(ruta,"r", encoding="utf-8") as f:
            lis_datos = json.load(f)
    except FileNotFoundError: 
        lis_datos = None
    except json.JSONDecodeError:
        lis_datos = []
    return lis_datos

def ALMACENAR_DATOS(ruta, datos):
    try:
        with open(ruta,"w", encoding="utf-8") as f:
            json.dump(datos, f) 
        print("Datos almacenados con éxito")
    except FileNotFoundError:
        print("No pudieron guardarse los datos correctamente, verifique el archivo.")

def VER_TAREAS(datos):
    i = 1
    for dato in datos:
        if dato["Estado"] == "Incompleta":
            print(f"{i}. {dato['Etiqueta']}: {dato['Estado']} [ ]\n")
        elif dato["Estado"] == "Completa":
            print(f"{i}. {dato['Etiqueta']}: {dato['Estado']} [✅]\n")
        i += 1

def AGREGAR_TAREA(datos):
    dicc_tarea = {}
    try:
        dicc_tarea["Etiqueta"] = input("Ingrese una etiqueta para la tarea: ")
        dicc_tarea["Estado"] = "Incompleta"
        datos.append(dicc_tarea)
    except:
        print("A ocurrido un error a la hora de crear la tarea, volver a intentar")
    return datos

def MODIFICAR_TAREA(datos):
    i = 0
    creado = False
    tarea_cambio = input("Indique etiqueta de la tarea (Si no quiere editar dejar en blanco): ")
    while not creado:
        if i == len(datos):
            print("\nNo se encontro la tarea, chequee la etiqueta")
            tarea_cambio = input("Comporuebe el nombre y los espacios (Si no quiere editar dejar en blanco): ")
            i = 0
        elif datos[i]["Etiqueta"].lower() == tarea_cambio.lower():
            datos[i]["Estado"] = "Completa"
            print(f"La tarea se modifico con éxito\n")
            creado = True
        elif tarea_cambio == "": 
            creado = True
        else:
            i += 1
    return datos

def BORRAR_TAREA(datos):
    i = 0
    encontrado = False
    tarea_borrar = input("Ingrese la etiqueta de la tarea (Si no quiere borrar dejar en blanco): ")
    while not encontrado:
        if i == len(datos):
            print("\nNo se encontro la tarea, chequee la etiqueta")
            tarea_borrar = input("Comporuebe el nombre y los espacios (Si no quiere borrar dejar en blanco): ")
            i = 0
        elif datos[i]["Etiqueta"].lower() == tarea_borrar.lower():
            eliminado = datos.pop(i)
            print(f"Se elimino con éxito la tarea {eliminado["Etiqueta"]}\n")
            encontrado = True
        elif tarea_borrar == "":
            encontrado = True
        else:
            i += 1
    return datos

def OPCIONES_USUARIO():
    print("Que desea realizar?")
    opcion = int(input("1. Ver tareas\n" \
    "2. Agregar tarea\n" \
    "3. Modificar tarea\n" \
    "4. Borrar tarea\n" \
    "5. Salir\n"))
    return opcion

ruta_json = Path(r"C:\Users\SANTINO\OneDrive\Escritorio\Proyectos Python Automatizacion\GestorDeTareas\lista_tareas.json")

lis_datos = CARGAR_DATOS_JSON(ruta_json)
if lis_datos == None:
    print("No se encontro el archivo para almacenar.")
else:
    salir = False
    while not salir:
        try:
            match OPCIONES_USUARIO():
                case 1:
                    VER_TAREAS(lis_datos)
                case 2:
                    lis_datos = AGREGAR_TAREA(lis_datos)
                case 3:
                    lis_datos = MODIFICAR_TAREA(lis_datos)
                case 4:
                    lis_datos = BORRAR_TAREA(lis_datos)
                case 5:
                    salir = True
                case _: 
                    print("Ingrese un número válido.\n")
        except ValueError:
            print("Ingrese un valor válido. \n")

    ALMACENAR_DATOS(ruta_json, lis_datos)