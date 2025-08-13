import pytest
from src.api_infinity_chess.generar_info_curso import solicitar_peticion_limite
from src.utils.headers.headers_grupo import headers_content_json
from src.utils.cargar_schema import cargar_schema
from src.assertions.add import assert_validar_response_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue MABUG001: No muestra mensaje de error al ingresar un id con formato invalido", run=True)
def test_obtener_los_limites_grupos_con_id_invalido_de_una_materia_sede_modulo4(get_url):
    logger.info("Iniciando test MAM015.")
    CODMATERIA ="135164825asdasda" #formato invalido
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    response = solicitar_peticion_limite(get_url,CODMATERIA,headers_content_json)
    logger.debug(response.json)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==400
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_grupos_limite.json"))
    logger.info("Test completado.")