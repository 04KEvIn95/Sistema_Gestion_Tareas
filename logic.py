from data import guardar_tareas


## Almacena las tareas cargadas en memoria durante la ejecución
tareas = []

## Controla la generación automática de identificadores únicos
contador_id = 1


def inicializar(datos):
    """
    Inicializa el sistema cargando las tareas existentes.
    """

    global tareas, contador_id
    tareas = datos

    ## Ajusta el contador tomando el ID más alto registrado
    if tareas:
        contador_id = max(t["id"] for t in tareas) + 1


def obtener_tareas():
    """
    Retorna la lista actual de tareas registradas.
    """

    return tareas


def agregar_tarea(titulo, descripcion):
    """
    Registra una nueva tarea en el sistema.
    """

    ## Verifica que el título no esté vacío
    if titulo == "":
        return False, "El título es obligatorio"

    global contador_id

    ## Crea la estructura de datos de la nueva tarea
    tarea = {
        "id": contador_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "estado": "Pendiente"
    }

    tareas.append(tarea)
    contador_id += 1

    ## Guarda los cambios realizados en el archivo JSON
    guardar_tareas(tareas)

    return True, "Tarea registrada"


def editar_tarea(indice, titulo, descripcion):
    """
    Modifica la información de una tarea existente.
    """

    ## Verifica que el título tenga contenido válido
    if titulo == "":
        return False, "El título es obligatorio"

    ## Actualiza los datos de la tarea seleccionada
    tareas[indice]["titulo"] = titulo
    tareas[indice]["descripcion"] = descripcion

    guardar_tareas(tareas)

    return True, "Tarea editada"


def eliminar_tarea(indice):
    """
    Elimina una tarea de la lista del sistema.
    """

    tareas.pop(indice)

    ## Guarda los cambios después de eliminar la tarea
    guardar_tareas(tareas)


def cambiar_estado(indice):
    """
    Cambia el estado de una tarea entre pendiente y completada.
    """

    estado = tareas[indice]["estado"]

    ## Alterna el estado actual de la tarea seleccionada
    if estado == "Pendiente":
        tareas[indice]["estado"] = "Completada"
    else:
        tareas[indice]["estado"] = "Pendiente"

    guardar_tareas(tareas)