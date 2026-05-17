## @file logic.py
#  @brief Módulo de interfaz gráfica para el Sistema de Gestión de Tareas.
#  @details Contiene la inicialización de la ventana de Tkinter, manejo de 
#           eventos de la UI y la interacción con el backend lógico.

import tkinter as tk
from tkinter import messagebox
import logic

## @brief Inicializa la aplicación y construye la interfaz gráfica de usuario.
#  @param datos Lista o estructura de datos con las tareas iniciales que se cargarán en el sistema.
def iniciar_app(datos):
    # Este código inicializa la lógica con los datos cargados
    logic.inicializar(datos)

    # Este código crea la ventana principal
    ventana = tk.Tk()
    ventana.title("Sistema de Gestión de Tareas")
    ventana.geometry("500x550")  # Se aumenta el tamaño para mejor espacio visual

    # ==============================
    # FUNCIONES UI
    # ==============================

    ## @brief Actualiza la lista visual de tareas en la interfaz.
    #  @details Borra el contenido actual del Listbox y vuelve a insertar
    #           todas las tareas obtenidas desde el módulo lógico.
    def actualizar_lista():
        # Este código actualiza la lista visual de tareas
        lista_tareas.delete(0, tk.END)

        for tarea in logic.obtener_tareas():
            texto = f"{tarea['id']} - {tarea['titulo']} [{tarea['estado']}]"
            lista_tareas.insert(tk.END, texto)

    ## @brief Limpia los campos de entrada de la interfaz.
    #  @details Borra el texto del campo de título y todo el contenido 
    #           del campo de descripción multilínea.
    def limpiar():
        # Este código limpia los campos de entrada
        entrada_titulo.delete(0, tk.END)

        # Este código limpia todo el contenido del campo de texto multilínea
        entrada_descripcion.delete("1.0", tk.END)

    ## @brief Obtiene el índice de la tarea seleccionada en el Listbox.
    #  @return int El índice de la tarea seleccionada si existe, de lo contrario devuelve None.
    def obtener_indice():
        # Este código obtiene el índice de la tarea seleccionada
        seleccion = lista_tareas.curselection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione una tarea")
            return None
        return seleccion[0]

    ## @brief Procesa el formulario para agregar una nueva tarea.
    #  @details Extrae los textos de la UI, invoca la lógica para guardar la tarea
    #           y muestra una alerta informando si el proceso fue exitoso o falló.
    def agregar():
        # Este código obtiene los datos del formulario
        titulo = entrada_titulo.get()

        # Este código obtiene el texto multilínea desde la posición inicial hasta el final
        descripcion = entrada_descripcion.get("1.0", tk.END).strip()

        ok, mensaje = logic.agregar_tarea(titulo, descripcion)

        if ok:
            actualizar_lista()
            limpiar()
            messagebox.showinfo("Éxito", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    ## @brief Modifica la tarea actualmente seleccionada.
    #  @details Recupera el índice seleccionado y los nuevos valores del formulario
    #           para actualizar la información de la tarea de forma persistente.
    def editar():
        indice = obtener_indice()
        if indice is None:
            return

        titulo = entrada_titulo.get()
        descripcion = entrada_descripcion.get("1.0", tk.END).strip()

        ok, mensaje = logic.editar_tarea(indice, titulo, descripcion)

        if ok:
            actualizar_lista()
            limpiar()
            messagebox.showinfo("Éxito", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    ## @brief Elimina la tarea actualmente seleccionada.
    #  @details Pide una confirmación visual al usuario antes de proceder a la
    #           eliminación en el backend.
    def eliminar():
        indice = obtener_indice()
        if indice is None:
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar tarea?"):
            logic.eliminar_tarea(indice)
            actualizar_lista()

    ## @brief Cambia el estado de la tarea seleccionada.
    #  @details Alterna el estado de la tarea (por ejemplo, de "Pendiente" a "Completada")
    #           e inmediatamente refresca los datos de la UI.
    def estado():
        indice = obtener_indice()
        if indice is None:
            return

        logic.cambiar_estado(indice)
        actualizar_lista()

    ## @brief Evento disparado al seleccionar un elemento de la lista.
    #  @param event Objeto que contiene información del evento de selección de Tkinter.
    #  @details Extrae los atributos de la tarea seleccionada y los vuelca en
    #           los campos de edición correspondientes de la pantalla.
    def cargar(event):
        # Este código carga los datos de la tarea seleccionada en el formulario
        seleccion = lista_tareas.curselection()
        if seleccion:
            tarea = logic.obtener_tareas()[seleccion[0]]

            entrada_titulo.delete(0, tk.END)
            entrada_titulo.insert(0, tarea["titulo"])

            # Este código limpia e inserta texto multilínea en el campo de descripción
            entrada_descripcion.delete("1.0", tk.END)
            entrada_descripcion.insert("1.0", tarea["descripcion"])

    # ==============================
    # INTERFAZ
    # ==============================

    frame = tk.Frame(ventana)
    frame.pack(pady=10)

    tk.Label(frame, text="Título").pack(anchor="w")
    entrada_titulo = tk.Entry(frame, width=45)
    entrada_titulo.pack(pady=5)

    tk.Label(frame, text="Descripción").pack(anchor="w")

    # Este código crea un campo de texto multilínea con ajuste automático de palabras
    entrada_descripcion = tk.Text(frame, width=45, height=6, wrap="word")
    entrada_descripcion.pack(pady=5)

    frame_btn = tk.Frame(ventana)
    frame_btn.pack(pady=10)

    tk.Button(frame_btn, text="Agregar", width=15, command=agregar).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(frame_btn, text="Editar", width=15, command=editar).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame_btn, text="Eliminar", width=15, command=eliminar).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(frame_btn, text="Estado", width=15, command=estado).grid(row=1, column=1, padx=5, pady=5)

    # Este código crea la lista donde se mostrarán las tareas
    lista_tareas = tk.Listbox(ventana)
    lista_tareas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    lista_tareas.bind("<<ListboxSelect>>", cargar)

    # Este código carga las tareas al iniciar
    actualizar_lista()

    # Este código mantiene la ventana en ejecución
    ventana.mainloop()