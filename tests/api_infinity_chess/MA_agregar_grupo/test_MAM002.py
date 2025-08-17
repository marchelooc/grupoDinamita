import pytest
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.api_infinity_chess.generar_info_curso import codigo_curso, realizar_peticion
from src.utils.payload.generar_payload_grupo import generar_payload_2_carac
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue MABUG001: Permite agregar una materia con 2 caracteres en el nombre", run=True)
def test_agregar_un_nuevo_grupo_con_nombre_dos_caracteres(get_url):
    logger.info("Iniciando test MAM002.")
    CODCURSO = codigo_curso(get_url)
    logger.debug(f"Curso seleccionado: {CODCURSO}")
    payload = generar_payload_2_carac(CODCURSO)
    logger.debug(f"payload: {payload}")
    response = realizar_peticion(get_url,payload)
    logger.info("Validando schema del payload.")
    assert_validar_schema_input(payload,cargar_schema("schema_grupo.json"))
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 400
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_grupo.json"))
    logger.info("Test completado.")