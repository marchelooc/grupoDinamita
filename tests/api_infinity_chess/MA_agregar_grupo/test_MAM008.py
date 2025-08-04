import pytest
import requests
import random

from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.api_infinity_chess.obtener_curso import obtener_cursos , obtener_nombre_grupo_existente
from src.utils.generador_codigo import  generar_cod, obtener_dias, obtener_horas, obtener_limite, obtener_precio
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
def test_agregar_grupo_duplicado_desde_existente(get_url):
    logger.info("Iniciando test MAM008.")
    # Obtener un curso válido
    lista_cursos = obtener_cursos(get_url)
    CODCURSO = random.choice(lista_cursos)["CODCURSO"]
    logger.debug(f"Curso seleccionado: {CODCURSO}")
    # Obtener nombre de un grupo ya creado
    nombre_grupo = obtener_nombre_grupo_existente(get_url, CODCURSO)

    # Crear payload duplicado
    payload = {
        "CODCURSO": CODCURSO,
        "CODSEDE": "Modulo 4",
        "NOMBREGRUPO": nombre_grupo, 
        "CODGRUPO": generar_cod(nombre_grupo),  # Cambia código pero mismo nombre
        "LIMITE": obtener_limite(),
        "PRECIO": obtener_precio(),
        "DIAS": obtener_dias(),
        "HORA": obtener_horas()
    }

    # Intentar crear duplicado
    url_final = get_url + "agregarGrupo"
    logger.info(f"Enviando POST a {url_final}.")
    response = requests.post(url_final, json=payload)
    logger.info("Validando schema del payload.")
    assert_validar_schema_input(payload,cargar_schema("schema_grupo.json"))
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 409
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_grupo.json"))
    logger.info("Test completado.")