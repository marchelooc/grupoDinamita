import pytest
from src.api_infinity_chess.generar_info_curso import solicitar_peticion_limite,validar_respuesta
from src.utils.headers.headers_grupo import headers_content_json
from src.utils.generador_codigo import generar_cod_caracteres
from src.utils.logger_config import logger

@pytest.mark.negative
def test_obtener_los_limites_grupos_con_id_con_caracteres_especiales_sede_modulo4(get_url):
    logger.info("Iniciando test MAM016.")
    CODMATERIA =generar_cod_caracteres()
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    response = solicitar_peticion_limite(get_url,CODMATERIA,headers_content_json)
    logger.debug(f"Este es el response: {response.json}")
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==404
    validar_respuesta(response)
    logger.info("Test completado.")