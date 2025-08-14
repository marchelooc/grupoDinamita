import pytest
from src.api_infinity_chess.obtener_trabajadores import obtener_codigo_de_trabajador_invalido
from src.api_infinity_chess.eliminar_trabajador import enviar_DELETE
from src.utils.logger_config import logger

@pytest.mark.negative
def test_intentar_eliminar_un_trabajador_con_un_CODTRABAJADOR_invalido (get_url):
    logger.info("Iniciando test SVT046.")
    response = enviar_DELETE (get_url, obtener_codigo_de_trabajador_invalido())
    logger.info(f"Codigo de respuesta DELETE: {response.status_code}")
    assert response.status_code == 404
    logger.info("Test completado.")