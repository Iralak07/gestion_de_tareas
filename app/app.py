import streamlit as st
from crud import add_task, list_tasks, mark_task_completed, delete_completed_tasks, delete_task_by_id

# Configuración inicial de la app
st.set_page_config(page_title="Gestión de Tareas", layout="centered")

def main():
    """
    Función principal de la aplicación de gestión de tareas.
    """
    st.title("Gestión de Tareas")
    menu = ["Agregar Tarea", "Lista de Tareas", "Eliminar Tareas Completadas"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Agregar Tarea":
        add_task_ui()
    elif choice == "Lista de Tareas":
        list_tasks_ui()
    elif choice == "Eliminar Tareas Completadas":
        delete_tasks_ui()


def add_task_ui():
    """
    Interfaz para agregar una tarea.
    """
    st.header("Agregar una Tarea")
    title = st.text_input("Título de la tarea")
    description = st.text_area("Descripción de la tarea")

    if st.button("Agregar Tarea"):
        if not title.strip():
            st.error("El título es obligatorio.")
            return

        try:
            add_task(title, description)
            st.success("¡Tarea agregada exitosamente!")
        except Exception as e:
            st.error(f"Error al agregar la tarea: {e}")


def list_tasks_ui():
    """
    Interfaz para listar tareas y marcarlas como completadas.
    """
    st.header("Lista de Tareas")
    try:
        tasks = list_tasks()
        if not tasks:
            st.info("No hay tareas registradas.")
            return

        for task in tasks:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"**{task.title}** - {'✅ Completada' if task.completed else '⏳ Pendiente'}")
            with col2:
                if not task.completed:
                    if st.button(f"✓ {task.id}", key=f"complete_{task.id}"):
                        try:
                            mark_task_completed(task.id)
                            st.success(f"Tarea {task.id} marcada como completada.")
                        except Exception as e:
                            st.error(f"Error al marcar como completada: {e}")
    except Exception as e:
        st.error(f"Error al cargar las tareas: {e}")


def delete_tasks_ui():
    """
    Interfaz para eliminar tareas completadas.
    """
    st.header("Eliminar Tareas Completadas")
    
    try:
        # Obtener todas las tareas
        tasks = list_tasks()
        # Filtrar tareas completadas
        completed_tasks = [task for task in tasks if task.completed]

        if not completed_tasks:
            st.info("No hay tareas completadas para eliminar.")
            return

        # Listar tareas completadas
        st.write("Tareas Completadas:")
        for task in completed_tasks:
            st.write(f"- {task.title} (ID: {task.id})")

        # Opción para eliminar todas las tareas completadas
        if st.button("Eliminar Todas las Tareas Completadas"):
            try:
                delete_completed_tasks()  # Eliminar todas las tareas completadas
                st.success("¡Todas las tareas completadas han sido eliminadas!")
            except Exception as e:
                st.error(f"Error al eliminar todas las tareas: {e}")

        # Opción para eliminar una tarea específica
        task_to_delete = st.selectbox("Selecciona una tarea para eliminar", [task.title for task in completed_tasks])
        if st.button("Eliminar Tarea Seleccionada"):
            # Buscar la tarea seleccionada por su título
            task_to_delete_obj = next(task for task in completed_tasks if task.title == task_to_delete)
            try:
                delete_task_by_id(task_to_delete_obj.id)  # Eliminar tarea por ID
                st.success(f"¡Tarea '{task_to_delete}' eliminada exitosamente!")
            except Exception as e:
                st.error(f"Error al eliminar la tarea '{task_to_delete}': {e}")

    except Exception as e:
        st.error(f"Error al cargar las tareas completadas: {e}")


if __name__ == "__main__":
    main()

