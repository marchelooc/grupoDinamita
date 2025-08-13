import pytest
from src.utils.generador_codigo import generar_codigo
from src.api_infinity_chess.eliminar_trabajador import enviar_DELETE
from src.utils.logger_config import logger

@pytest.mark.negative
def test_intentar_eliminar_un_trabajador_con_un_CODTRABAJADOR_inexistente (get_url):
    logger.info("Iniciando test SVT045.")
    logger.info("Obtener un CODTRABAJADOR inexistente.")
    CODTRABAJADOR = generar_codigo ()
    logger.debug(f"Trabajador elegido: {CODTRABAJADOR}.")
    response = enviar_DELETE (get_url, CODTRABAJADOR)
    logger.info(f"Codigo de respuesta DELETE: {response.status_code}")
    assert response.status_code == 404
    logger.info("Test completado.")

#Intentar eliminar un trabajador con un CODTRABAJADOR inexistente