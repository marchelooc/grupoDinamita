import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT_con_headers
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_actualizar_todos_los_datos_de_un_trabajador_existente_con_valores_validos (get_url):
    logger.info("Iniciando de test SVT041.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar(trabajador)
    logger.debug(payload)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT_con_headers(get_url, payload, trabajador, headers)
    assert response.status_code == 403
    logger.info("Test completado.")





#Intentar actualizar datos con el Content-type en formato TEXT-PLAIN. 