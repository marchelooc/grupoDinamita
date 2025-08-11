import pytest
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.api_infinity_chess.generar_info_curso import codigo_curso, realizar_peticion
from src.utils.payload.generar_payload_grupo import cargar_payload_grupo
from src.utils.generador_codigo import obtener_nombre_grupo, generar_cod, obtener_dias, obtener_limite, obtener_precio
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue MABUG004: Se permite agregar un grupo con un horario fuera de rango", run=True)
def test_agregar_un_nuevo_grupo_con_horario_invalido(get_url):
    logger.info("Iniciando test MAM005.")
    CODCURSO = codigo_curso(get_url)
    logger.debug(f"Curso seleccionado: {CODCURSO}")
    nombre_grupo=obtener_nombre_grupo()
    dias=obtener_dias()
    precio=obtener_precio()
    limite=obtener_limite()
    codigo=generar_cod(nombre_grupo)
    payload = cargar_payload_grupo(CODCURSO,nombre_grupo,dias,"23:00",precio,limite,codigo)
    logger.debug(payload)
    response = realizar_peticion(get_url,payload)
    logger.info("Validando schema del payload.")
    assert_validar_schema_input(payload,cargar_schema("schema_grupo.json"))
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 400
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_grupo.json"))
    logger.info("Test completado.")