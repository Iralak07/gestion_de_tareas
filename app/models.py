from sqlalchemy import Column, Integer, String, Boolean
from database import Base, engine


class Task(Base):
    """
    Modelo de Tarea.
    Representa una tarea con un título, descripción opcional y estado de completitud.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    title = Column(String, nullable=False, comment="Título de la tarea")
    description = Column(String, nullable=True, comment="Descripción opcional de la tarea")
    completed = Column(Boolean, default=False, nullable=False, comment="Estado de la tarea: completada o no")

    def __repr__(self):
        """
        Representación legible del objeto Task.
        """
        return f"<Task(id={self.id}, title='{self.title}', completed={self.completed})>"

    def to_dict(self):
        """
        Convierte el objeto Task en un diccionario para facilitar el manejo de datos.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }


# Crear las tablas en la base de datos (si no existen)
def init_db():
    """
    Inicializa la base de datos, creando las tablas definidas en los modelos.
    """
    try:
        Base.metadata.create_all(engine)
        print("Tablas creadas exitosamente.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")


# Inicializa la base de datos
if __name__ == "__main__":
    init_db()
