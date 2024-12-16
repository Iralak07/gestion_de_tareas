from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Configuración de la base de datos
DATABASE_URL = "sqlite:///tasks.db"

# Crear motor de base de datos
try:
    engine = create_engine(DATABASE_URL, echo=False, future=True)  # `echo` para depuración, `future` para compatibilidad futura
    print("Motor de base de datos creado exitosamente.")
except SQLAlchemyError as e:
    print(f"Error al crear el motor de base de datos: {e}")
    raise

# Base declarativa
Base = declarative_base()

# Crear una sesión
def get_session():
    """
    Crea y devuelve una nueva sesión de base de datos.
    """
    try:
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return SessionLocal()
    except SQLAlchemyError as e:
        print(f"Error al crear la sesión de base de datos: {e}")
        raise

# Prueba de conexión
def test_connection():
    """
    Prueba la conexión a la base de datos.
    """
    session = None
    try:
        session = get_session()
        session.execute("SELECT 1")  # Ejecuta una consulta simple para verificar la conexión
        print("Conexión a la base de datos establecida exitosamente.")
    except SQLAlchemyError as e:
        print(f"Error al conectar con la base de datos: {e}")
        raise
    finally:
        if session:
            session.close()


# Prueba de inicialización
if __name__ == "__main__":
    test_connection()
