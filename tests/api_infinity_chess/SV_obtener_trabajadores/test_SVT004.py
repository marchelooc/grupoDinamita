import requests
import pytest
import random
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajadores
from src.utils.logger_config import logger

@pytest.mark.negative
def test_verificar_que_la_URL_incorrecta_retorne_error_404(get_url):
    lista_trabajdores = obtener_trabajadores(get_url)
    CODTRABAJADOR = random.choice(lista_trabajdores)["CODTRABAJADOR"]
    logger.debug(f"Trabajador buscado: {CODTRABAJADOR}.")
    endpoint = "obtenerTrabajadorees/" + CODTRABAJADOR #Endpoint mal escrito intencionalente
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 404
    logger.info("Test completado.")