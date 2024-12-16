# Gestion de Tareas

La tarea consiste en el desarrollo de una aplicación para gestionar tareas diarias. La aplicación ha sido desarrollada en el lenguaje de programación Python, utilizando Streamlit para la interfaz gráfica y SQLite como base de datos, gestionada a través del ORM SQLAlchemy.

En cuanto al entorno de trabajo, estoy utilizando virtaulenv para gestionar los paquetes, tanto de python, sqlalchemy y Streamlit.

## Entorno de Trabajo

### Instalacion de Virtualenv 
  - pip install virtualenv
### Creando un entorno
  - virtualenv -p python3 venv
### Activando el entorno virtual
  - Linux: source nombre_del_entorno/bin/activate
  - Windows: .\nombre_del_entorno\Scna 

Una vez que tenemos el entorno virtual activado, nos queda descargar el repositorio ubicado en github, esto nos traera una carpeta que contiene varios archivos


## Instalando dependencias

Una vez descargado el repositorio, nos dirigimos a la carpeta con el nombre "gestion_de_tares", en el mismo existe una estructura de esta manera.

    app/                   # Carpeta principal del proyecto
    │
    ├── app.py             # Archivo principal que inicia la aplicación.
    ├── crud.py            # Contiene las funciones CRUD (Create, Read, Update, Delete) para gestionar los datos.
    ├── database.py        # Configuración de la base de datos, incluyendo la conexión y el manejo del ORM.
    ├── models.py          # Definición de los modelos de datos utilizados por la base de datos.
    ├── requirements.txt   # Archivo que especifica las dependencias necesarias para el proyecto.
    ├── .gitignore         # Archivo para ignorar archivos y carpetas específicas al usar Git.


Nos dirigimos a la carpeta principal del proyecto, el cual es app/ dentro del mismo instalamos las dependencias necesarias para la ejecucion del proyecto.

    pip install -r requirements.txt


Una vez instaladas las dependencias, no queda mas que ejecutar., pero antes dare una explicacion a grandes rasgos de cada uno de los archivos.


### Archivo app.py 

  El archivo app.py es el núcleo de una aplicación desarrollada con Streamlit, una biblioteca de Python para construir interfaces de usuario interactivas. La aplicación implementa un sistema de gestión de tareas diarias que permite al usuario agregar tareas, listar tareas, marcarlas como completadas y eliminarlas.
Contenido del archivo

    Importaciones
        streamlit para crear la interfaz gráfica de usuario.
        Funciones CRUD (add_task, list_tasks, mark_task_completed, delete_completed_tasks, delete_task_by_id) importadas del módulo crud, que manejan la interacción con la base de datos.

    Configuración inicial
        Configura la aplicación con un título ("Gestión de Tareas") y un diseño centrado mediante st.set_page_config.

    Estructura del flujo
    La lógica de la aplicación está organizada en funciones específicas que cumplen diferentes propósitos:
        main():
            Define la navegación de la aplicación mediante un menú en la barra lateral (st.sidebar.selectbox).
            Muestra las interfaces correspondientes a las opciones seleccionadas en el menú: agregar tareas, listar tareas o eliminar tareas completadas.
        add_task_ui():
            Muestra un formulario para agregar tareas con un título y descripción.
            Valida el título y, si es válido, llama a la función add_task del módulo crud.
        list_tasks_ui():
            Recupera y muestra todas las tareas utilizando la función list_tasks.
            Ofrece opciones para marcar tareas como completadas, con botones dinámicos por cada tarea.
        delete_tasks_ui():
            Enumera las tareas completadas.
            Permite eliminar todas las tareas completadas o una específica seleccionada por el usuario.

    Técnicas utilizadas
        Componentes dinámicos:
        Utiliza elementos de Streamlit, como st.button, st.text_input, st.selectbox, y st.columns, para crear una interfaz interactiva que se adapta a las acciones del usuario.
        Control de excepciones:
        Implementa bloques try-except para manejar errores en las operaciones CRUD, mostrando mensajes de error específicos si algo falla.
        Estado de tareas:
        Las tareas se presentan con diferentes estados (Pendiente, Completada) y se administran de manera eficiente utilizando funciones específicas del módulo crud.
        Lógica basada en eventos:
        Las acciones del usuario (clics en botones, selecciones) activan funciones específicas, lo que implementa un flujo interactivo.

    Ejecución del programa
    El archivo define su punto de entrada con el bloque if __name__ == "__main__":, asegurando que la función main() solo se ejecute si el script es ejecutado directamente.

Flujo de ejecución

    Inicio de la aplicación (main):
        Muestra el título de la aplicación y el menú lateral.
        Según la opción seleccionada en el menú, llama a la función correspondiente:
            "Agregar Tarea" → add_task_ui
            "Lista de Tareas" → list_tasks_ui
            "Eliminar Tareas Completadas" → delete_tasks_ui

    Agregar una tarea (add_task_ui):
        El usuario ingresa el título y la descripción de una nueva tarea.
        Al hacer clic en "Agregar Tarea", valida el título y utiliza la función add_task para guardar la tarea.

    Listar tareas (list_tasks_ui):
        Recupera todas las tareas mediante list_tasks.
        Muestra el estado de cada tarea (Pendiente/Completada).
        Incluye un botón por tarea para marcarla como completada.

    Eliminar tareas completadas (delete_tasks_ui):
        Recupera tareas completadas mediante list_tasks.
        Permite al usuario eliminarlas individualmente o todas juntas utilizando delete_task_by_id o delete_completed_tasks.

Técnicas utilizadas

    Programación modular:
        Cada funcionalidad está separada en funciones (add_task_ui, list_tasks_ui, etc.), lo que facilita el mantenimiento y escalabilidad del código.

    Interactividad con Streamlit:
        Streamlit ofrece una interfaz dinámica, permitiendo que los cambios en el estado del usuario (como clics o entradas) actualicen la vista instantáneamente.

    Integración con el backend:
        La lógica de interacción con la base de datos está delegada a las funciones CRUD importadas del módulo crud, separando las preocupaciones de la lógica de interfaz y la manipulación de datos.

    Control de errores robusto:
        Los bloques try-except aseguran que los errores, como problemas de conexión con la base de datos, se manejen de forma clara y amigable para el usuario.

    Diseño centrado en el usuario:
        La interfaz es intuitiva, con mensajes de error claros, opciones fáciles de usar y un diseño limpio que guía al usuario en cada paso.


### Archivo CRUD.py

El archivo crud.py implementa las operaciones CRUD (Crear, Leer, Actualizar y Eliminar) para una aplicación de gestión de tareas. Estas funciones interactúan con la base de datos utilizando SQLAlchemy como ORM (Object-Relational Mapping) para realizar consultas y transacciones. Las operaciones se realizan sobre un modelo llamado Task, que representa las tareas en la base de datos.
Estructura y flujo del archivo

    Importaciones necesarias:
        get_session: Función para obtener una sesión de base de datos.
        Task: Modelo de base de datos que representa una tarea.
        SQLAlchemyError: Excepción para manejar errores relacionados con SQLAlchemy.

    Funciones CRUD y flujo principal:
        Cada función realiza las operaciones necesarias sobre la tabla Task mediante una sesión de SQLAlchemy. Al final de cada operación, la sesión se cierra automáticamente, asegurando que los recursos se liberen correctamente.

Funciones del archivo

1. add_task(title, description)

    Propósito: Crear y guardar una nueva tarea en la base de datos.
    Flujo:
        Se inicia una sesión.
        Se crea una instancia de Task con el título y la descripción proporcionados.
        Se agrega la tarea a la sesión y se realiza el commit.
        En caso de error, la transacción se revierte (rollback) y se lanza una excepción.
    Técnicas utilizadas:
        Manejo de errores con try-except.
        Transacciones con commit y rollback.
        Contexto seguro para garantizar el cierre de la sesión.

2. list_tasks()

    Propósito: Obtener todas las tareas almacenadas en la base de datos.
    Flujo:
        Se inicia una sesión.
        Se realiza una consulta para obtener todas las filas de la tabla Task.
        En caso de error, se lanza una excepción.
    Técnicas utilizadas:
        Consulta ORM: Uso de session.query(Task).all() para recuperar múltiples registros.
        Manejo de excepciones.

3. mark_task_completed(task_id)

    Propósito: Marcar una tarea como completada mediante su ID.
    Flujo:
        Se inicia una sesión.
        Se busca una tarea específica usando un filtro por ID.
        Si se encuentra, se actualiza el estado de la tarea (completed = True) y se confirma la transacción.
        Si no se encuentra, se imprime un mensaje.
    Técnicas utilizadas:
        Filtros en consultas: Uso de .filter(Task.id == task_id).
        Actualización de registros.

4. edit_task(task_id, title, description)

    Propósito: Editar los detalles de una tarea existente.
    Flujo:
        Se busca la tarea por ID.
        Si existe, se actualizan los campos de título y descripción.
        Se confirma la transacción.
    Técnicas utilizadas: Similar a las anteriores, con actualizaciones explícitas de atributos.

5. delete_completed_tasks()

    Propósito: Eliminar todas las tareas que hayan sido marcadas como completadas.
    Flujo:
        Se realiza una consulta para filtrar tareas completadas (Task.completed == True).
        Se eliminan las tareas coincidentes y se confirma la transacción.
    Técnicas utilizadas:
        Eliminación en bloque: Uso de .delete() para múltiples filas.

6. delete_task_by_id(task_id)

    Propósito: Eliminar una tarea específica mediante su ID.
    Flujo:
        Se busca la tarea por ID.
        Si se encuentra, se elimina.
        Se confirma la transacción.
    Técnicas utilizadas: Similar a la función de eliminación masiva, pero con un enfoque individual.


### Archivo database.py


El archivo database.py contiene la configuración y las herramientas necesarias para conectar y manejar la base de datos en una aplicación basada en SQLAlchemy. Sirve como la capa de infraestructura que configura el motor, las sesiones y la base declarativa para la interacción con la base de datos.
Estructura y componentes principales

    Configuración de la base de datos:
        Define el URL de la base de datos como sqlite:///tasks.db. Esto indica que la base de datos SQLite se almacena en un archivo local llamado tasks.db.
        Proporciona opciones para la conexión como echo para depuración y future para garantizar compatibilidad con futuras versiones de SQLAlchemy.

    Creación del motor de la base de datos:
        Utiliza create_engine de SQLAlchemy para establecer el motor de base de datos que sirve como interfaz entre SQLAlchemy y la base de datos real.

    Declarative Base:
        Utiliza declarative_base() para definir un punto de partida para los modelos ORM (Objetos Relacionales).

    Creación de sesiones:
        Define una función llamada get_session que devuelve sesiones de base de datos para ejecutar consultas y transacciones.

    Prueba de conexión:
        Incluye la función test_connection que verifica si la conexión a la base de datos se puede establecer correctamente.

    Prueba al ejecutar el archivo directamente:
        Si el archivo se ejecuta como programa principal, llama a test_connection() para comprobar que la configuración y conexión son correctas.

### Archivo models.py

Este archivo define el modelo Task para representar tareas en la base de datos y contiene funciones para inicializar las tablas necesarias.
Estructura y componentes principales

    Modelo Task:
        Representa una tarea con los siguientes atributos:
            id: Identificador único (clave primaria).
            title: Título obligatorio de la tarea.
            description: Descripción opcional.
            completed: Estado de completitud (por defecto, False).
        Métodos:
            __repr__: Proporciona una representación legible del objeto.
            to_dict: Convierte la instancia en un diccionario para facilitar el manejo de datos.

    Creación de tablas:
        Utiliza Base.metadata.create_all(engine) para crear las tablas definidas en los modelos si no existen.

    Inicialización de la base de datos (init_db):
        Verifica y crea las tablas, manejando posibles errores.

    Ejecución directa:
        Si el archivo se ejecuta directamente, llama a init_db para crear las tablas.


### Archivo utils.py

El archivo utils.py contiene funciones útiles para exportar e importar tareas desde y hacia un archivo JSON, interactuando con una base de datos SQL a través de SQLAlchemy. Estas funciones se apoyan en otras funciones, como list_tasks y add_task, que están definidas en el archivo crud.py. A continuación te proporciono una descripción detallada de su contenido:
Funciones del archivo utils.py
1. export_tasks_to_json(file_path)

Esta función exporta todas las tareas existentes a un archivo JSON.

    Parámetros:
        file_path: Especifica la ruta donde se guardará el archivo JSON que contendrá las tareas exportadas.

    Funcionamiento:
        Utiliza la función list_tasks() para obtener todas las tareas de la base de datos.
        Convierte cada tarea en un diccionario mediante el método to_dict() (que debe estar implementado en los modelos de tarea).
        Abre el archivo en modo escritura (w) y guarda los datos usando json.dump(), con una indentación de 4 espacios para mejorar la legibilidad.
        Si ocurre algún error durante la operación, se captura y muestra un mensaje de error.

    Manejo de errores:
        Captura errores de la base de datos (SQLAlchemyError) si hay problemas al obtener las tareas de la base de datos.
        También captura otros tipos de excepciones generales para asegurar que cualquier error durante el proceso sea manejado y registrado.

2. import_tasks_from_json(file_path)

Esta función importa tareas desde un archivo JSON y las guarda en la base de datos.

    Parámetros:
        file_path: Especifica la ruta del archivo JSON desde el cual se cargarán las tareas.

    Funcionamiento:
        Abre el archivo JSON en modo lectura (r) y carga su contenido utilizando json.load(), que convierte el archivo en una lista de diccionarios.
        Itera sobre cada tarea en la lista y utiliza la función add_task() para agregar la tarea a la base de datos. Se asegura de que si no hay una descripción en el archivo JSON, se pase una descripción vacía por defecto.
        Al finalizar, imprime un mensaje indicando que las tareas fueron importadas exitosamente.

    Manejo de errores:
        Si el archivo no se encuentra, se captura el error FileNotFoundError y se imprime un mensaje adecuado.
        Si el archivo JSON está mal formado y no se puede decodificar, se captura el error json.JSONDecodeError.
        Si ocurre un error al guardar las tareas en la base de datos, se captura un error SQLAlchemyError.
        También captura cualquier otro tipo de excepción general que pueda ocurrir durante el proceso.


### Ejecutemos y probemos la aplicacon

  A fin de ejecutar nuestra aplicacion utilizaremos el siguiente comanda:

    - streamlit run app.py

  En la cosola se vera esto si todo va bien:

  ![Screenshot from 2024-12-16 18-58-50](https://github.com/user-attachments/assets/d23b3623-cecd-4615-b4f1-967e5cd13df4)


  Automaticamente se abrira el navegador predeterminado, mostrando la siguiente pantalla: Se pide encarecidamente utilizar el modo oscuro en su navegador.. 

   ![Screenshot from 2024-12-16 19-01-30](https://github.com/user-attachments/assets/a778bd4a-e005-4d4d-af90-34c51a96fb28)

 Si nos situamos en la parte superior izquierda se puede observar un menu desplegable con las siguientes opcion:

 ![Screenshot from 2024-12-16 19-04-07](https://github.com/user-attachments/assets/e715bed9-a6d2-42a7-959c-a87780d90287)


  La primera opcions es la de Agregar Tarea, el cual se puede observar en la imagen anterior.
  La Segunda opcion es la de listar Tareas,que se encarga de traer todas las listas que se encuentran en la Base de datos.

  ![Screenshot from 2024-12-16 19-07-12](https://github.com/user-attachments/assets/31170d34-0279-42a2-a159-7af5396377f0)

  La Tercera opcion muestra las tareas que ya estan completadas, con la opcion de eliminar de a uno o eliminarlos todos de una vez.

  ![Screenshot from 2024-12-16 19-08-35](https://github.com/user-attachments/assets/feeb5baf-3661-4267-b809-76f9cf401e5b)


  La cuarta opcion te da la capcidad de exportar todas las tareas pendientes en un archivo .json el cual se alojo en la carpeta raiz del proyecto.
  
  ![Screenshot from 2024-12-16 19-10-59](https://github.com/user-attachments/assets/945ae9a7-fc41-4413-8c33-248b7a05efc6)

  La Quinta opcion, importa desde un archivo .json tareas directamente cargando en la base de datos una vez completada la importacion.

  ![Screenshot from 2024-12-16 19-12-10](https://github.com/user-attachments/assets/2810b3ca-21c3-427e-9e01-b55c5b9e23a3)
