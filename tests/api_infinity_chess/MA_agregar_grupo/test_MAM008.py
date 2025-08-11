import pytest
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.api_infinity_chess.generar_info_curso import codigo_curso, realizar_peticion, crear_grupo
from src.utils.payload.generar_payload_grupo import cargar_payload_grupo
from src.utils.generador_codigo import  generar_cod, obtener_dias
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MABUG005: Esta manejando incorrectamente el response enviando error 500 y no 409", run=True)
def test_agregar_grupo_duplicado_desde_existente(get_url):
    logger.info("Iniciando test MAM008.")
    CODCURSO = codigo_curso(get_url)
    logger.debug(f"Curso seleccionado: {CODCURSO}")
    crear_grupo(get_url,CODCURSO)
    nombre_grupo="grupo doble"
    dias=obtener_dias()
    codigo= generar_cod(nombre_grupo)
    payload=cargar_payload_grupo(CODCURSO,nombre_grupo,dias,"18:00",100,20,codigo)
    logger.debug(payload)
    response = realizar_peticion(get_url,payload)
    logger.info("Validando schema del payload.")
    assert_validar_schema_input(payload,cargar_schema("schema_grupo.json"))
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 409
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_grupo.json"))
    logger.info("Test completado.")