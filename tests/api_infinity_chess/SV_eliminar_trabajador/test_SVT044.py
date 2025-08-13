import pytest
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajador_aleatorio
from src.api_infinity_chess.eliminar_trabajador import enviar_DELETE
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_eliminar_un_trabajador_existente_con_CODTRABAJADOR_valido (get_url):
    logger.info("Iniciando test SVT044.")
    logger.info("Obtener un trabajador existente aleatorio.")
    CODTRABAJADOR = obtener_trabajador_aleatorio (get_url)
    logger.debug(f"Trabajador elegido: {CODTRABAJADOR}.")
    response = enviar_DELETE (get_url, CODTRABAJADOR)
    logger.info(f"Codigo de respuesta DELETE: {response.status_code}")
    assert response.status_code == 200
    logger.info("Test completado.")
    
#Eliminar un trabajador existente con CODTRABAJADOR válido