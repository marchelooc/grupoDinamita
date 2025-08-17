import pytest
from src.api_infinity_chess.generar_info_curso import realizar_eliminacion, validar_respuesta
from src.utils.logger_config import logger

@pytest.mark.negative
def test_verificar_que_se_elimine_un_grupo_con_id_vacio(get_url):
    logger.info("Iniciando test MAM021.")
    codigo=""
    logger.info(f"Enviando un codigo vacio{codigo}")
    response = realizar_eliminacion(get_url,codigo)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==404
    validar_respuesta(response)
    logger.info("Test completado.")