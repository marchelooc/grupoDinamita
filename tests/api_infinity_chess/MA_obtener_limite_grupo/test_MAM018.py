import pytest
from src.api_infinity_chess.generar_info_curso import codigo_curso, solicitar_peticion_limite
from src.utils.headers.headers_grupo import headers_accept_text_plain
from src.utils.cargar_schema import cargar_schema
from src.assertions.add import assert_validar_response_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MABUG013: El endpoint ignora Accept: text/plain y responde JSON en lugar de texto plano o 406", run=True)
def test_validar_comportamiento_con_accept_text_plain_header(get_url):
    logger.info("Iniciando test MAM018.")
    CODMATERIA = codigo_curso(get_url)
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    response = solicitar_peticion_limite(get_url,CODMATERIA,headers_accept_text_plain)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==406
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_grupos_limite.json"))
    logger.info("Test completado.") 