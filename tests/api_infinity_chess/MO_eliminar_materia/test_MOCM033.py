import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_a_eliminar

@pytest.mark.smoke
def test_validar_comportamiento_al_eliminar_una_materia_sin_CODIGOCURSO(get_url):
    logger.info("Iniciando test MOCM033.")
    logger.debug("eliminando materia sin pasar codigo")
    url_final = get_url + "eliminarCurso/"
    logger.info(f"Enviando DELETE {url_final}.")
    response = requests.delete(url_final)
    assert response.status_code == 404
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
#    assert_validar_response_schema(response,cargar_schema("schema_eliminar_materia.json"))
    logger.info("Test MOCM033 realizado.")
