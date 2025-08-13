import pytest
from src.api_infinity_chess.eliminar_trabajador import enviar_POST_para_DELETE
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajador_aleatorio
from src.utils.logger_config import logger

@pytest.mark.negative
def test_intentar_eliminar_un_trabajador_usando_POST_en_lugar_de_DELETE (get_url):
    logger.info("Iniciando test SVT048.")
    logger.info("Obtener un trabajador existente aleatorio.")
    CODTRABAJADOR = obtener_trabajador_aleatorio (get_url)
    logger.debug(f"Trabajador elegido: {CODTRABAJADOR}.")
    response = enviar_POST_para_DELETE (get_url, CODTRABAJADOR)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 405
    logger.info("Test completado.")

#Intentar eliminar un trabajador usando POST en lugar de DELETE