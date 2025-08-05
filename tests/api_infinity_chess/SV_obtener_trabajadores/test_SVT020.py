import requests
import pytest
import random
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajadores
from src.utils.logger_config import logger

@pytest.mark.negative
def test_obtener_trabajador_usando_POST_en_lugar_de_GET(get_url):
    lista_trabajadores = obtener_trabajadores(get_url)
    CODTRABAJADOR = random.choice(lista_trabajadores)["CODTRABAJADOR"]
    logger.debug(f"Prueba POST sobre ID (que sólo admite GET): {CODTRABAJADOR}")
    endpoint = f"obtenerTrabajador/{CODTRABAJADOR}"
    url = get_url + endpoint
    logger.info(f"Enviando POST a {url}(endpoint diseñado para GET)")
    response = requests.post(url)
    logger.info(f"Codigo de respuesta: {response.status_code}")
    assert response.status_code == 405, ( f"Se obtuvo el codigo {response.status_code}")
    logger.info("Test completado.")
