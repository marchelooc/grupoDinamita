Instrucciones de ejecucion test case: 
1. Instalacion de entorno vitual:
    python -m venv venv
2. Activacion de entorno virtual:
    venv\Scripts\activate 
3. Instalacion de requirements
    pip install -r requirements.txt
4. Crear archivo .env con el contenido:
    PYTHONPATH=.
5. Ejecución de test cases general:
    pytest tests/api_infinity_chess
6. Ejecución de test cases general con reporte:
    pytest tests/api_infinity_chess --html=report.html --self-contained-html -v
7. Ejecución de test cases por historias de usuario:
    pytest tests/api_infinity_chess/FM_agregar_registro_inscripcion (Falta)
    pytest tests/api_infinity_chess/FM_obtener_lista_estudiantes (Falta)
    pytest tests/api_infinity_chess/MA_agregar_grupo
    pytest tests/api_infinity_chess/MA_obtener_grupo
    pytest tests/api_infinity_chess/MO_agregar_materia
    pytest tests/api_infinity_chess/MO_verificar_la_materia
    pytest tests/api_infinity_chess/RP_lista_tutores_por_sede
    pytest tests/api_infinity_chess/RP_registrar_motivo_por_tutor
    pytest tests/api_infinity_chess/SS_cambiar_estado_de_tutor
    pytest tests/api_infinity_chess/SS_obtener_tutores_activos
    pytest tests/api_infinity_chess/SV_crear_trabajador
    pytest tests/api_infinity_chess/SV_obtener_trabajadores
8. Ejecución de test cases por historias de usuario con reportes:
    pytest tests/api_infinity_chess/FM_agregar_registro_inscripcion --html=report.html --self-contained-html -v (Falta)
    pytest tests/api_infinity_chess/FM_obtener_lista_estudiantes --html=report.html --self-contained-html -v (Falta)
    pytest tests/api_infinity_chess/MA_agregar_grupo --html=report.html --self-contained-html -v
    pytest tests/api_infinity_chess/MA_obtener_grupo --html=report.html --self-contained-html -v
    pytest tests/api_infinity_chess/MO_agregar_materia --html=report.html --self-contained-html -v
    pytest tests/api_infinity_chess/MO_verificar_la_materia --html=report.html --self-contained-html -v
    pytest tests/api_infinity_chess/RP_lista_tutores_por_sede --html=report.html --self-contained-html -v
    pytest tests/api_infinity_chess/RP_registrar_motivo_por_tutor --html=report.html --self-contained-html -v
    pytest tests/api_infinity_chess/SS_cambiar_estado_de_tutor --html=report.html --self-contained-html -v
    pytest tests/api_infinity_chess/SS_obtener_tutores_activos --html=report.html --self-contained-html -v
    pytest tests/api_infinity_chess/SV_crear_trabajador --html=report.html --self-contained-html -v
    pytest tests/api_infinity_chess/SV_obtener_trabajadores --html=report.html --self-contained-html -v
9. Ejecución por tipo de mark:
    pytest -m smoke
    pytest -m negative
    pytest -m functional
    pytest -m regression

Test Plan Infinity Chess

Descripción del producto
    Infinity Chess es una aplicación desarrollada para apoyar la gestión administrativa de un instituto, optimizando y centralizando diversos procesos clave. Esta herramienta permite gestionar eficientemente estudiantes y tutores, aplicar filtros de búsqueda avanzados, crear y administrar materias junto con sus respectivos grupos, así como inscribir estudiantes en los grupos disponibles. Su diseño está orientado a mejorar la organización institucional y facilitar el trabajo del personal administrativo.

Objetivos
    El objetivo de las pruebas automatizadas en el sistema Infinity Chess es asegurar la calidad y estabilidad de la aplicación mediante la verificación continua de sus funcionalidades clave. A través de estas pruebas se busca validar que los módulos de gestión de estudiantes, tutores, materias y trabajadores funcionen conforme a los requerimientos definidos

Funcionalidades
    Como equipo de automatización, se realizarán los siguientes módulos en dos sprints establecidos.
    
    Módulo Lista Estudiante/Tutor
    Este módulo permite gestionar la información de estudiantes y tutores registrados, incluyendo la edición de datos, la asignación de grupos y materias, así como la visualización de las relaciones entre ambos. Está diseñado para facilitar el trabajo de los roles administrativos, por lo que su acceso está habilitado exclusivamente para el Director, el Gerente y la Secretaria.
    
    Módulo de Materias
    Este módulo permite la creación de materias y la asignación de grupos correspondientes a cada una. Su acceso está habilitado exclusivamente para los usuarios con los roles de Director, Gerente y Secretaria 
    
    Módulo de Trabajadores
    Este módulo permite registrar y gestionar al personal del instituto, enfocándose específicamente en maestros y secretarias. Su funcionalidad incluye la administración de datos relevantes para cada perfil, y está disponible exclusivamente para los usuarios con rol de Director y Gerente.

Tipos de pruebas
    A continuación, se describen las pruebas seleccionadas para este ciclo de evaluación:

    Pruebas exploratorias
    Se ejecutan sin guiones predefinidos, permitiendo descubrir comportamientos inesperados.  En este caso, se utilizarán comandos cURL con payload como cuerpo para verificar la respuesta de los servicios REST. tecnicas campos vacíos, diagrama de estados (datos inválidos, equivalencia y valores límite, campos vacíos)

    Pruebas de Humo (“Smoke testing”)
    Validan que las funciones principales del sistema operen correctamente del tipo (“Happy path”)

    Pruebas funcionales
    Evalúan si el sistema cumple con los requisitos funcionales establecidos, verificando entradas, salidas y comportamientos esperados. pruebas (positivas, negativas)

    Pruebas de regresión
    Se aplican después de cambios en el sistema para asegurar que las funcionalidades existentes no se vean afectadas.

Alcance y Limitaciones
    Durante los dos sprints se abordará el desarrollo de los siguientes módulos como usuario Director, cada uno con sus respectivos responsables:
    Validación de endpoints GET, POST, PUT, DELETE.
    Verificación de respuestas esperadas (200, 201, 400, 404, 422, 409 , 415).
    Casos de prueba positivos, negativos, campos vacíos y valores límite.
    Automatización de pruebas usando Python.
    Validación de endpoints con Path Params.
    Validación de endpoint con y sin Headers.
    Validación de endpoints con schemas.
    Validación de endpoints con payloads.
    urlBase = Infinity Chess

    Pruebas por sprint
    Primer Sprint
        Módulo de Listas: 
        Endpoints: 
        {{urlBase}}/obtenerEstudiantes/{sede} (GET)
        {{urlBase}}/obtenerTutores/{sede} (GET)
        {{urlBase}}/obtenerTutoresActivos (GET)
        {{urlBase}}/obtenerTutoresEstudiante/{id} (GET)
        {{urlBase}}/obtenerEstudiantesTutor/{id} (GET)
        {{urlBase}}/agregarMotivo (POST)
        {{urlBase}}/agregarRegistro (POST)
        {{urlBase}}/actualizarTutor/{id} (PUT)
        {{urlBase}}/acutalizarEstadoTutor/{id} (POST)
        {{urlBase}}/actualizarEstudiante/{id} (PUT)
        Encargados: Sergio, Ronald, Fernando.
        Módulo de Materias: 
        Endpoints: 
        {{urlBase}}/obtenerGrupo/{id}/{sede} (GET)
        {{urlBase}}/verificarCurso/{id} (GET)
        {{urlBase}}/agregarCurso (POST)
        {{urlBase}}/agregarGrupo (POST)
        Encargados: Miguel, Marcelo
        Módulo de Trabajadores 
        Endpoints: 
        {{urlBase}}/obtenerTrabajador/{id} (GET)
        {{urlBase}}/agregarTrabajador (POST)
        Encargado: Simón.

    Segundo Sprint

        Módulo de Listas: 
        Endpoints: 
        {{urlBase}}/obtenerEstudiantes/{sede} (GET)
        {{urlBase}}/obtenerTutores/{sede} (GET)
        {{urlBase}}/obtenerTutoresEstudiante/{id} (GET)
        {{urlBase}}/obtenerEstudiantesTutor/{id} (GET)
        {{urlBase}}/obtenerHorarioEstudiante/{id} (GET)
        {{urlBase}}/agregarMotivo (POST)
        {{urlBase}}/agregarRegistro (POST)
        {{urlBase}}/actualizarTutor/{id} (PUT)
        {{urlBase}}/actualizarEstudiante/{id} (PUT)
        {{urlBase}}/actualizarEstadoEstudiante/{id} (PUT)
        Encargados: Sergio, Ronald, Fernando.
        Módulo de Materias: 
        Endpoints: 
        {{urlBase}}/obtenerCurso/{id} (GET)
        {{urlBase}}/obtenerGrupoLimite/{id}/{sede} (GET)
        {{urlBase}}/eliminarCurso (DELETE)
        {{urlBase}}/eliminarGrupo (DELETE)
        Encargados: Miguel, Marcelo
        Módulo de Trabajadores 
        Endpoints: 
        {{urlBase}}/actualizarDatosTrabajador/{id} (PUT)
        {{urlBase}}/eliminarTrabajador/{id} (DELETE)
        Encargado: Simón.

Recursos
    QA Lead: Marcelo Ortuño Carreño.
    Scrum Master: Saul Fernando Mollo Murillo
    GIT Lead: Sergio Brayan Soliz Nogales
    Equipo de desarrollo: 	
        Ronald Marcelo Panigua Cordova
        Saul Fernando Mollo Murillo
        Simón Pedro Valdez Mamani
        Sergio Brayan Soliz Nogales
        Miguel Angel Alcón Yujra
        Marcelo Ortuño Carreño
    PO/PM: Rina Espinoza.

