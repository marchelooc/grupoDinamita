import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.materia import eliminar_materia

@pytest.mark.smoke

def test_validar_comportamiento_al_eliminar_materia_inexistente(get_url):
    logger.info("Iniciando test MOCM031.")
    logger.debug("eliminando materia inexistente con cod 2030NOEXIST")
    response = eliminar_materia(get_url, "2030NOEXIST")
    assert response.status_code == 404
    logger.info("Test MOCM031 realizado.")