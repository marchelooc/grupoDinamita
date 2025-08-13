import pytest
from src.api_infinity_chess.eliminar_trabajador import enviar_DELETE_sin_CODTRABAJADOR
from src.utils.logger_config import logger

@pytest.mark.negative
def test_intentar_eliminar_un_trabajador_sin_enviar_el_CODTRABAJADOR (get_url):
    logger.info("Iniciando test SVT047.")
    response = enviar_DELETE_sin_CODTRABAJADOR (get_url)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404
    logger.info("Test completado.")

#Intentar eliminar un trabajador sin enviar el CODTRABAJADOR