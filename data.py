## Este archivo se encarga de guardar y cargar los datos del sistema
import json
import os
import sys


## Obtiene la carpeta donde se ejecuta la aplicación
BASE_DIR = os.path.dirname(
    sys.executable if getattr(sys, 'frozen', False) else __file__
)

## Define la ruta completa del archivo donde se almacenan las tareas
ARCHIVO = os.path.join(BASE_DIR, "tareas.json")


def guardar_tareas(tareas):
    """
    Guarda la lista de tareas en el archivo JSON del sistema.
    """

    try:
        with open(ARCHIVO, "w") as archivo:
            json.dump(tareas, archivo, indent=4)

    except:
        ## Muestra un mensaje si ocurre un error durante el guardado
        print("Error al guardar las tareas")


def cargar_tareas():
    """
    Carga las tareas almacenadas previamente en el archivo JSON.
    """

    ## Verifica si el archivo de tareas existe
    if os.path.exists(ARCHIVO):

        try:
            with open(ARCHIVO, "r") as archivo:
                return json.load(archivo)

        except:
            ## Controla errores durante la lectura del archivo
            print("Error al cargar las tareas")
            return []

    ## Retorna una lista vacía si el archivo no existe
    return []