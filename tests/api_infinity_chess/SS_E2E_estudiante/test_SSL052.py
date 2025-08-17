import pytest
from src.utils.logger_config import logger 
from src.api_infinity_chess.E2E_estudiante import  crear_estudiante, obtener_estudiante,actualizar_estudiante,eliminar_estudiante

@pytest.mark.smoke
def test_E2E_estudiante(get_url):
     logger.info("Iniciando test SSL052.")
     logger.info("Crear nuevo estudiante.")
     cod_estudiante = crear_estudiante(get_url)
     logger.info("Obtener estudiante creado.")
     estudiante = obtener_estudiante(get_url, cod_estudiante)
     logger.info("Editar datos estudiante.")
     estudiante_actualizado = actualizar_estudiante(get_url,estudiante[0])
     logger.info("Eliminar estudiante.")
     eliminar_estudiante(get_url,estudiante_actualizado.get("CODESTUDIANTE"))
     logger.info("Obtener estudiante creado.")
     estudiante = obtener_estudiante(get_url, cod_estudiante)
     logger.info("Test completado.")