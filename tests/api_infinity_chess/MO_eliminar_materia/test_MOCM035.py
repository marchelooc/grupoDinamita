import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_a_eliminar, headers_text

@pytest.mark.smoke
def test_validar_comportamiento_al_eliminar_una_materia_con_header_text(get_url):
    logger.info("Iniciando test MOCM035.")
    logger.debug("creando curso para eliminar: Mecatronica con cod 2025MECA")
    url_final = get_url + "agregarCurso"
    requests.post(url_final, json=payload_materia_a_eliminar)
    logger.debug("eliminando Mecatronica con cod 2025MECA")
    url_final = get_url + "eliminarCurso/2025MECA"
    logger.info(f"Enviando DELETE {url_final}.")
    response = requests.delete(url_final, headers=headers_text)
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_eliminar_materia.json"))
    logger.info("Test MOCM035 realizado.")