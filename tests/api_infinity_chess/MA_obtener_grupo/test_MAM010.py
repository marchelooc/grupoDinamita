import requests
import json
import pytest
import random

from src.utils.cargar_schema import cargar_schema
from src.assertions.add import assert_validar_response_schema
from src.utils.logger_config import logger

@pytest.mark.negative
def test_obtener_grupos_de_una_materia_con_id_invalido_sede_modulo4(get_url):
    logger.info("Iniciando test MAM010.")
    #cursos=obtenerCursos(getUrl)
    CODMATERIA ="abcde"
    end_point = "obtenerGrupo/"+CODMATERIA+"/Modulo 4"
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    lista_url = get_url + end_point
    logger.info(f"Enviando GET a {lista_url}.")
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.get(lista_url, headers=headers)
    logger.debug(response.json)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_grupos.json"))
    logger.info("Test completado.")