import pytest
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import headers_json
from src.api_infinity_chess.materia import recuperar_cursos_sede_con_header

@pytest.mark.functional
def test_obtener_materias_de_una_sede_con_header_de_tipo_json(get_url):
    logger.info("Iniciando test MOCM005.")
    logger.debug("sede seleccionada: Modulo 4")
    response = recuperar_cursos_sede_con_header(get_url, "Modulo 4", headers_json)
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 200
    logger.debug(f"Código de respuesta: {response.status_code}.")
    logger.info("Test MOCM005 realizado.")
     
