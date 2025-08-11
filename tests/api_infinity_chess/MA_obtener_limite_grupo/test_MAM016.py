import pytest
from src.api_infinity_chess.generar_info_curso import solicitar_peticion
from src.utils.headers.headers_grupo import headers_content_json
from src.utils.generador_codigo import generar_cod_caracteres
from src.utils.cargar_schema import cargar_schema
from src.assertions.add import assert_validar_response_schema
from src.utils.logger_config import logger

@pytest.mark.negative
def test_obtener_los_limites_grupos_con_id_invalido_de_una_materia_sede_modulo4(get_url):
    logger.info("Iniciando test MAM016.")
    CODMATERIA =generar_cod_caracteres() #caracteres especiales
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    response = solicitar_peticion(get_url,CODMATERIA,headers_content_json)
    logger.debug(response.json)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==404
    try:
        data = response.json()
    except ValueError:
        data = None 
    if data:
        logger.info("Validando schema del response.")
        assert_validar_response_schema(data, cargar_schema("schema_lista_grupos_limite.json"))
    logger.info("Test completado.")