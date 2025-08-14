import pytest
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.api_infinity_chess.generar_info_curso import codigo_curso, realizar_peticion, crear_grupo_duplicado
from src.utils.payload.generar_payload_grupo import generar_payload_duplicado
from src.utils.cargar_schema import cargar_schema
from src.utils.response_500 import response_500
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MABUG005: Esta manejando incorrectamente el response enviando error 500 y no 409", run=True)
def test_agregar_grupo_duplicado_desde_existente(get_url):
    logger.info("Iniciando test MAM008.")
    CODCURSO = codigo_curso(get_url)
    logger.debug(f"Curso seleccionado: {CODCURSO}")
    nombre_grupo=crear_grupo_duplicado(get_url,CODCURSO)
    payload=generar_payload_duplicado(CODCURSO,nombre_grupo)
    logger.debug(f"payload: {payload}")
    response = realizar_peticion(get_url,payload)
    logger.info("Validando schema del payload.")
    assert_validar_schema_input(payload,cargar_schema("schema_grupo.json"))
    logger.info(f"Código de respuesta: {response.status_code}.")
    response_500(response)
    assert response.status_code == 409
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_grupo.json"))
    logger.info("Test completado.")