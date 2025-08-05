import requests
import pytest
from src.assertions.add import assert_validar_schema_input, assert_validar_response_schema
from src.utils.generador_codigo import generar_nom_materia, generar_cod
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=True)
def test_agregar_una_materia_con_headers_de_tipo_texto_plano(get_url):
    logger.info("Iniciando test MOCM022.")
    nombre_materia = generar_nom_materia()
    codigo_materia = generar_cod(nombre_materia)
    logger.debug(f"Curso aleatorio creado {nombre_materia}.")
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": codigo_materia,
                "CURSO": nombre_materia, 
                "ESTADO": "activo",
                }
    headers = {
            "Accept": "application/json",
            "Content-Type": "text/plain",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)"
    }
    logger.debug(f"este es el payload generado:{payload}")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload,cargar_schema("schema_materias.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST {url_final}.")
    response = requests.post(url_final, json=payload, headers=headers)
    assert response.status_code == 415
    logger.info(f"Código de respuesta: {response.status_code}.")
#    logger.info("Validando schema del response.")
#    assert_validar_response_schema(response,cargar_schema("schema_materias.json"))
    logger.info("Test MOCM022 realizado.")
#mostrar que materia fue creada 