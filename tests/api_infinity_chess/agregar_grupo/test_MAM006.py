import requests
import pytest
import random

from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.api_infinity_chess.obtener_curso import obtener_cursos
from src.utils.generador_codigo import obtener_nombre_grupo, generar_cod, obtener_dias, obtener_horas, obtener_limite
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_agregar_un_nuevo_grupo_con_precio_cero(getUrl):
    logger.info("Iniciando test MAM006.")
    lista_cursos = obtener_cursos(getUrl)
    CODCURSO = random.choice(lista_cursos)["CODCURSO"]
    logger.debug(f"Curso seleccionado: {CODCURSO}")
    end_point = "agregarGrupo"
    nombre_grupo=obtener_nombre_grupo()
    dias=obtener_dias()
    horas=obtener_horas()
    precio=0
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
    
    url_final = getUrl + end_point
    logger.info(f"Enviando POST a {url_final}.")
    response = requests.post(url_final, json=payload)
    logger.info("Validando schema del payload.")
    assert_validar_schema_input(payload,cargar_schema("schema_grupo.json"))
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 201
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_grupo.json"))
    logger.info("Test completado.")