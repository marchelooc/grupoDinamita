import pytest
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_estudiantes import enviar_solicitud
from src.api_infinity_chess.cambiar_estado_estudiante import obtener_estudiante_aleatorio

@pytest.mark.functional
def test_verificación_del_código_de_respuesta(get_url):
    logger.info("Iniciando test SSL019.")
    cod_estudiante = obtener_estudiante_aleatorio (get_url)
    logger.debug(f"Estudiante seleccionado: {cod_estudiante}.")
    response = enviar_solicitud(get_url,cod_estudiante)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.debug(f"Response: {response.json()}")
    logger.info("Test completado.")
    