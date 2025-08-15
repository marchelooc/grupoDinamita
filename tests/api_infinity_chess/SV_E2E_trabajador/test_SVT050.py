import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.E2E_trabajador import  crear_trabajador_E2E, obtener_trabajador_E2E, actualizar_trabajador_E2E, eliminar_trabajador_E2E

@pytest.mark.smoke
def test_E2E_estudiante(get_url):
    logger.info("Iniciando test SVT051")
    logger.info ("Crear un nuevo trabajador")
    codigo_trabajador = crear_trabajador_E2E (get_url)
    logger.info("Obtener al trabajador creado")
    trabajador = obtener_trabajador_E2E (get_url, codigo_trabajador)
    logger.info("Editar los datos del trabajador creado.")
    trabajador_actualizado = actualizar_trabajador_E2E (get_url, trabajador)
    logger.info("Obtener al trabajador creado, despues de editar sus datos")
    trabajador = obtener_trabajador_E2E (get_url, codigo_trabajador)
    logger.info("Eliminar al trabajador creado.")
    eliminar_trabajador_E2E(get_url,trabajador_actualizado["CODTRABAJADOR"])
    logger.info("Test completado.")