from data import cargar_tareas
from ui import iniciar_app

## Carga las tareas almacenadas previamente en el sistema
datos = cargar_tareas()

## Inicia la interfaz principal de la aplicación
iniciar_app(datos)