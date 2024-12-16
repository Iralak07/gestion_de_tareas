from database import get_session
from models import Task
from sqlalchemy.exc import SQLAlchemyError





# Agregar una tarea
def add_task(title, description):
    session = get_session()
    try:
        new_task = Task(title=title, description=description)
        session.add(new_task)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al agregar la tarea: {e}")
        raise
    finally:
        session.close()


# Listar tareas
def list_tasks():
    session = get_session()
    try:
        tasks = session.query(Task).all()
        return tasks
    except SQLAlchemyError as e:
        print(f"Error al listar las tareas: {e}")
        raise
    finally:
        session.close()


# Marcar tarea como completada
def mark_task_completed(task_id):
    session = get_session()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            task.completed = True
            session.commit()
        else:
            print(f"Tarea con ID {task_id} no encontrada.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al marcar la tarea como completada: {e}")
        raise
    finally:
        session.close()


# Editar una tarea
def edit_task(task_id, title, description):
    '''
    Función para editar las tareas.
    Requiere el ID de la tarea, el título y la descripción.
    '''
    session = get_session()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            task.title = title
            task.description = description
            session.commit()
        else:
            print(f"Tarea con ID {task_id} no encontrada.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al editar la tarea: {e}")
        raise
    finally:
        session.close()


# Eliminar tareas completadas
def delete_completed_tasks():
    session = get_session()
    try:
        session.query(Task).filter(Task.completed == True).delete()
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al eliminar las tareas completadas: {e}")
        raise
    finally:
        session.close()

def delete_task_by_id(task_id):
    """
    Elimina una tarea específica por su ID.
    """
    session = get_session()
    try:
        # Buscar la tarea por su ID
        task_to_delete = session.query(Task).filter(Task.id == task_id).first()

        if not task_to_delete:
            raise ValueError(f"Tarea con ID {task_id} no encontrada.")

        # Eliminar la tarea
        session.delete(task_to_delete)
        session.commit()
        print(f"Tarea con ID {task_id} eliminada exitosamente.")

    except ValueError as ve:
        print(ve)
        raise
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al eliminar la tarea: {e}")
        raise
    finally:
        session.close()

