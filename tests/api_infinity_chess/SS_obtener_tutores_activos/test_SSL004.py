import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_tutores import enviarSolicitud, verificar_tutores_activos

@pytest.mark.functional
def test_verificación_del_código_de_respuesta(get_url):
    logger.info("Iniciando test SSL004.")
    response = enviarSolicitud(get_url)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.info("Test completado.")