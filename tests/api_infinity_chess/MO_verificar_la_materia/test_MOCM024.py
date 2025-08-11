import requests
import pytest
from src.utils.response_500 import response_500
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_validar_comportamiento_obetener_materias_con_nombres_repetidos(get_url):
    logger.info("Iniciando test MOCM024.")
    endpoint = "verificarCurso/" + "MateriaRepetida"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    response = requests.get(lista_url)
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response")
    assert_validar_response_schema(response,cargar_schema("schema_lista_materias.json")) 
    respuestaJSON = response.json()
    cursos_filtrados = [item for item in respuestaJSON if item.get("CURSO") == "MateriaRepetida"]
    logger.info(f"La cantidad de cursos con nombre repetido de MateriaRepetida es de: {len(cursos_filtrados)}.")
    assert len(cursos_filtrados) >= 2
    logger.info("Test MOCM024 realizado.")
