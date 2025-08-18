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
10. Ejecucion todo:
    pytest -n 1 
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
Evalúan si el sistema cumple con los requisitos funcionales establecidos, verificando entradas, salidas y comportamientos esperados.
Pruebas negativas
Es una técnica de prueba de software que ingresa intencionadamente entradas no válidas o datos inesperados para ver cómo el software maneja estos escenarios.
Pruebas de regresión
Se aplican después de cambios en el sistema para asegurar que las funcionalidades existentes no se vean afectadas.
Alcance y Limitaciones
Durante los dos sprints se abordará el desarrollo de los siguientes módulos como usuario Director, cada uno con sus respectivos responsables:
Validación de endpoints GET, POST, PUT, DELETE.
Verificación de respuestas esperadas (200,400, 404, 500).
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
{{urlBase}}/obtenerTutores/{sede} (GET)
{{urlBase}}/obtenerTutoresActivos (GET)
{{urlBase}}/obtenerTutoresEstudiante/{id} (GET)
{{urlBase}}/obtenerEstudiantesTutor/{id} (GET)
{{urlBase}}/agregarMotivo (POST)
{{urlBase}}/actualizarTutor/{id} (PUT)
{{urlBase}}/acutalizarEstadoTutor/{id} (POST)
{{urlBase}}/actualizarEstudiante/{id} (PUT)
Encargados: Sergio, Ronald.
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
Carry Over
{{urlBase}}/verificarCurso/{id} (GET)
Módulo de Listas: 
Endpoints: 
{{urlBase}}/obtenerEstudiantes/{sede} (GET)
{{urlBase}}/obtenerTutores/{sede} (GET)
{{urlBase}}/obtenerEstudiantesTutor/{id} (GET)
{{urlBase}}/obtenerHorarioEstudiante/{id} (GET)
{{urlBase}}/agregarMotivo (POST)
{{urlBase}}/agregarRegistro (POST)
{{urlBase}}/actualizarTutor/{id} (PUT)
{{urlBase}}/actualizarEstadoEstudiante/{id} (PUT)
{{urlBase}}/agregarRegistro (POST)
Encargados: Sergio, Ronald.
Módulo de Materias: 
Endpoints: 
{{urlBase}}/obtenerCursos/{sede} (GET)
{{urlBase}}/obtenerGrupoLimite/{id}/{sede} (GET)
{{urlBase}}/eliminarCurso (DELETE)
{{urlBase}}/eliminarGrupo (DELETE)
Encargados: Miguel, Marcelo
Módulo de Trabajadores 
Endpoints: 
{{urlBase}}/actualizarDatosTrabajador/{id} (PUT)
{{urlBase}}/eliminarTrabajador/{id} (DELETE)
Encargado: Simón.
E2E
E2E Curso:
{{urlBase}}/agregarCurso (POST)
{{urlBase}}/verificarCurso/{id} (GET)
{{urlBase}}/eliminarCurso (DELETE)
{{urlBase}}/obtenerCursos/{sede} (GET)
E2E Grupo
{{urlBase}}/agregarGrupo (POST)
{{urlBase}}/obtenerGrupo/{id}/{sede} (GET)
{{urlBase}}/eliminarGrupo (DELETE)
E2E Trabajador
{{urlBase}}/agregarTrabajador (POST)
{{urlBase}}/obtenerTrabajador/{CODTRABAJADOR} (GET)
{{urlBase}}/actualizarDatosTrabajador/{CODTRABAJADOR} (PUT)
{{urlBase}}/obtenerTrabajador/{CODTRABAJADOR} (GET)
{{urlBase}}/eliminarTrabajador/{CODTRABAJADOR} (DELETE)
E2E Tutor
{{urlBase}}/agregarTutor (POST)
{{urlBase}}/obtenerTutor/CODTUTOR (GET)
{{urlBase}}/actualizarTutor/CODTUTOR (PUT)
{{urlBase}}/eliminarTutor/CODTUTOR (DELETE)
E2E Estudiante
{{urlBase}}/agregarEstudiante (POST)
{{urlBase}}/obtenerEstudiante/CODESTUDIANTE (GET)
{{urlBase}}/actualizarEstudiante/CODESTUDIANTE (PUT)
{{urlBase}}/eliminarTutor/CODTUTOR (DELETE)
Herramientas
Como parte del entorno de pruebas y gestión de calidad, se emplearán diversas herramientas que permiten automatizar procesos, documentar resultados y coordinar actividades entre los miembros del equipo. Las herramientas seleccionadas para este proyecto son:
Python: Lenguaje de programación utilizado para desarrollar scripts de prueba y automatización de servicios REST.
Pytest: Framework de pruebas en Python que facilita la ejecución de casos de prueba, la validación de respuestas y la integración con otras herramientas.
VS Code: Editor de código, usado para múltiples lenguajes de programación. Soporta Python y cuenta con extensiones útiles para la automatización.
Jira: Plataforma de gestión de proyectos que permite organizar tareas, registrar incidencias y hacer seguimiento del progreso del equipo.
Zephyr: Complemento de Jira orientado a la gestión de pruebas, que permite documentar casos, planificar ejecuciones y vincular resultados con los requerimientos del sistema.
Google Drive: Servicio de almacenamiento en la nube, para guardar, compartir y colaborar en los documentos del proyecto.
Postman: Herramienta para probar APIs REST. Permite hacer peticiones (GET, POST, etc.), ayudando en la automatización de pruebas y endpoints de forma sencilla.
Dev Console: Herramienta del navegador web que permite inspeccionar elementos HTML, revisar errores JavaScript, ver tráfico de red (requests), y depurar aplicaciones web.
Notepad: Herramienta usada para sacar los schemas

Cronograma

Recursos
Para el desarrollo y ejecución del proyecto, se cuenta con un equipo multidisciplinario que desempeña roles clave en cada etapa del proceso:
QA Lead: Marcelo Ortuño Carreño, responsable de liderar las actividades de aseguramiento de calidad.
Jira lead: Miguel Angel Alcón Yujra
Scrum Master: Simón Pedro Valdez Mamani
GIT Lead: Sergio Brayan Soliz Nogales
Equipo de desarrollo: 	Ronald Marcelo Panigua Cordova
Simón Pedro Valdez Mamani
Sergio Brayan Soliz Nogales
Miguel Angel Alcón Yujra
Marcelo Ortuño Carreño
PO/PM: Rina Espinoza, quien asume el rol de Product Owner y Project Manager.


