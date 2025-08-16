import pytest
from src.api_infinity_chess.generar_info_curso import codigo_curso, solicitar_peticion_limite
from src.utils.headers.headers_grupo import headers_content_json
from src.utils.cargar_schema import cargar_schema
from src.assertions.add import assert_validar_response_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_obtener_limites_grupos_con_id_valido_de_una_materia_sede_modulo4(get_url):
    logger.info("Iniciando test MAM014.")
    CODMATERIA = codigo_curso(get_url)
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    response = solicitar_peticion_limite(get_url,CODMATERIA,headers_content_json)
    logger.debug(response.json)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_grupos_limite.json"))
    logger.info("Test completado.") 