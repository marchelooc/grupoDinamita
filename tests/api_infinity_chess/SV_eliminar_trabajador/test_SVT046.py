import pytest
from src.api_infinity_chess.eliminar_trabajador import enviar_DELETE
from src.utils.logger_config import logger

@pytest.mark.negative
def test_intentar_eliminar_un_trabajador_con_un_CODTRABAJADOR_invalido (get_url):
    logger.info("Iniciando test SVT046.")
    logger.info("Obtener un CODTRABAJADOR invalido.")
    CODTRABAJADOR = "29010378CLAUD"
    logger.debug(f"Trabajador elegido: {CODTRABAJADOR}.")
    response = enviar_DELETE (get_url, CODTRABAJADOR)
    logger.info(f"Codigo de respuesta DELETE: {response.status_code}")
    assert response.status_code == 404
    logger.info("Test completado.")

#Intentar eliminar un trabajador con un CODTRABAJADOR invalido