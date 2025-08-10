import requests
import pytest
from src.utils.response_500 import response_500
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG009: El sistema no procesa ni reconoce la solicitud", run=True)
def test_crear_un_trabajador_sin_body_para_el_post (get_url):
    endpoint = "agregarTrabajador"
    url = get_url + endpoint
    logger.info(f"Enviando POST a {url}")
    response = requests.post(url)
    logger.info(f"Código de respuesta: {response.status_code}")
    response_500(response)
    assert response.status_code == 400, (f"Codigo de respuesta {response.status_code}")
    logger.info("Test completado.")
