import requests
import pytest
import random

from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.api_infinity_chess.obtener_curso import obtener_cursos
from src.utils.generador_codigo import generar_cod, obtener_dias, obtener_horas, obtener_limite, obtener_precio
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue MABUG003: Esta manejando incorrectamente el codigo de error en el response", run=True)
def test_agregar_un_nuevo_grupo_con_40_caracteres_en_nombre(get_url):
    logger.info("Iniciando test MAM004.")
    lista_cursos = obtener_cursos(get_url)
    CODCURSO = random.choice(lista_cursos)["CODCURSO"]
    logger.debug(f"Curso seleccionado: {CODCURSO}")
    end_point = "agregarGrupo"
    nombre_grupo="Este es el nombre de grupo con muy largo"
    dias=obtener_dias()
    horas=obtener_horas()
    precio=obtener_precio()
    limite=obtener_limite()
    codigo=generar_cod(nombre_grupo)
    payload = {
        "CODCURSO": CODCURSO,
        "CODSEDE": "Modulo 4",
        "NOMBREGRUPO": nombre_grupo, 
        "CODGRUPO": codigo,
        "LIMITE" :limite,
        "PRECIO":precio,
        "DIAS" : dias,
        "HORA":horas} 
    logger.debug(payload)
    url_final = get_url + end_point
    logger.info(f"Enviando POST a {url_final}.")
    response = requests.post(url_final, json=payload)
    logger.info("Validando schema del payload.")
    assert_validar_schema_input(payload,cargar_schema("schema_grupo.json"))
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 400
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_grupo.json"))
    logger.info("Test completado.")