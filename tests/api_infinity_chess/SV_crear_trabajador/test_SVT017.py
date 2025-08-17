import pytest
from src.api_infinity_chess.crear_trabajador import enviar_POST_textplain
from src.utils.payload.payload_crear_trabajador import crear_payload_valido
from src.utils.response_500 import response_500
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG007: El formato text plain no es soportado por el sistema", run=True)
def test_crear_un_trabajador_con_content_type_text_plain (get_url):
    logger.info("Iniciando test SVT017.")
    logger.info("Obtener datos de un trabajador para registrarlo en el sistema.")
    payload = crear_payload_valido()
    logger.debug(f"Payload:{payload}.")
    response = enviar_POST_textplain(get_url, payload, headers=None)
    logger.debug(f"Response:{response.json()}.")
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 415
    logger.info("Metodo incorrecto.")