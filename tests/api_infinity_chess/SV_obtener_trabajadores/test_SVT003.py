import requests
import pytest
from src.utils.logger_config import logger

@pytest.mark.negative
def test_obtener_trabajador_sin_enviar_Id(get_url):
    endpoint = "obtenerTrabajador/"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404
    logger.info("Test completado.")