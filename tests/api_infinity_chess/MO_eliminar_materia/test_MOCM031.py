import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke

def test_validar_comportamiento_al_eliminar_materia_inexistente(get_url):
    logger.info("Iniciando test MOCM031.")
    logger.debug("eliminando materia inexistente con cod 2030NOEXIST")
    url_final = get_url + "eliminarCurso/2030NOEXIST"
    logger.info(f"Enviando DELETE {url_final}.")
    response = requests.delete(url_final)
    assert response.status_code == 404
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_eliminar_materia.json"))
    logger.info("Test MOCM031 realizado.")