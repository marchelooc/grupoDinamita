import pytest
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.api_infinity_chess.generar_info_curso import codigo_curso, realizar_peticion
from src.utils.payload.generar_payload_grupo import generar_payload_nom_largo
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue MABUG003: El endpoint /agregarGrupo devuelve 500 en vez de 400 cuando NOMBREGRUPO excede la longitud permitida", run=True)
def test_agregar_un_nuevo_grupo_con_40_caracteres_en_nombre(get_url):
    logger.info("Iniciando test MAM004.")
    CODCURSO = codigo_curso(get_url)
    logger.debug(f"Curso seleccionado: {CODCURSO}")
    payload = generar_payload_nom_largo(CODCURSO)
    logger.debug(f"payload: {payload}")
    response = realizar_peticion(get_url,payload)
    logger.info("Validando schema del payload.")
    assert_validar_schema_input(payload,cargar_schema("schema_grupo.json"))
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 400
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_grupo.json"))
    logger.info("Test completado.")