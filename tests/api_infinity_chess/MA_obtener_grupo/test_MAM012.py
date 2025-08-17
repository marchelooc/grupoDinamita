import pytest
from src.api_infinity_chess.generar_info_curso import codigo_curso, solicitar_peticion
from src.utils.headers.headers_grupo import headers_accept_html
from src.utils.cargar_schema import cargar_schema
from src.assertions.add import assert_validar_response_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MABUG006: Esta manejando incorrectamente el codigo de error en el response se esperaba 406", run=True)
def test_obtener_grupos_de_una_materia_con_cabecera_accept_text_html(get_url):
    logger.info("Iniciando test MAM012.")
    CODMATERIA = codigo_curso(get_url)
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    response = solicitar_peticion(get_url,CODMATERIA,headers_accept_html)
    logger.debug(f"response:{response.json()}")
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==406
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_grupos.json"))
    logger.info("Test completado.")
    