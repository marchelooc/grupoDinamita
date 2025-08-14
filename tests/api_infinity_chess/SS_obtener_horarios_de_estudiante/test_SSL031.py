import pytest
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_estudiantes import enviar_solicitud
from src.utils.generador_codigo import generar_codigo

@pytest.mark.negative
def test_estudiante_inexistente(get_url):
     logger.info("Iniciando test SSL031.")
     logger.info("Obtener un estudiante no registrado.")
     cod_estudiante = generar_codigo()
     logger.debug(f"Estudiante seleccionado: {cod_estudiante}.")
     response = enviar_solicitud(get_url,cod_estudiante)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 404
     logger.info("Test completado.")