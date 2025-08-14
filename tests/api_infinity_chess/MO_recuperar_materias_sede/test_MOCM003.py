import requests
import pytest
import random
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_validar_comportamiento_al_recuperar_cursos_de_sede_sin_nombre(get_url):
    logger.info("Iniciando test MOCM001.")
    logger.debug("sede seleccionada: vacio")
    endpoint = "obtenerCursos/"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    response = requests.get(lista_url)
    assert response.status_code == 404
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    try:
        assert_validar_response_schema(response, cargar_schema("schema_lista_materias_sede.json"))
    except requests.exceptions.JSONDecodeError:
        pytest.skip("La respuesta no contiene JSON, omitiendo validación de schema")
    logger.info("Test MOCM001 realizado.")

    
