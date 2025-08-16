import requests
import pytest
from src.utils.logger_config import logger

@pytest.mark.functional
def test_validar_respuesta_al_obtener_materias_de_sede_sin_materias(get_url):
    logger.info("Iniciando test MOCM001.")
    logger.debug("sede seleccionada: Modulo 5")
    endpoint = "obtenerCursos/Modulo 5"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    response = requests.get(lista_url)
    logger.info(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Test MOCM001 realizado.")
    
