import requests
import pytest

from src.assertions.add import assert_validar_schema_input
from src.utils.generador_codigo import generar_nom_materia, generar_cod
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=False)
def test_validar_el_limite_maximo_de_caracteres_del_campo_CODCURSO(get_url):
    logger.info("Iniciando test MOCM013.")
    nombre_materia = generar_nom_materia()
    codigo_materia = generar_cod(nombre_materia)
    logger.debug(f"Curso aleatorio creado {nombre_materia}.")
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": codigo_materia + "123456789",
                "CURSO": nombre_materia, 
                "ESTADO": "activo",
                }
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload,cargar_schema("schema_materias.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST {url_final}.")
    response = requests.post(url_final, json=payload)
    assert response.status_code == 400
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Test MOCM013 realizado.")

    