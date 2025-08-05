import requests
import pytest
import random
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajadores
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_verificar_que_la_estructura_sea_completa_en_la_respuesta (get_url):
    lista_trabajadores = obtener_trabajadores(get_url)
    CODTRABAJADOR = random.choice(lista_trabajadores)["CODTRABAJADOR"]
    logger.debug(f"Trabajador buscado: {CODTRABAJADOR}.")
    url = f"{get_url}obtenerTrabajador/{CODTRABAJADOR}"
    logger.info(f"Enviando GET a {url}.")
    response = requests.get(url)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response, cargar_schema("schema_obtener_trabajador.json"))

    trabajador = response.json()
    if isinstance(trabajador, list):
        assert trabajador, "La lista contiene los datos del trabajador"
        trabajador = trabajador[0]
    campos_requeridos = [
        "CODTRABAJADOR",
        "NOMBRETRABAJADOR",
        "FECHANACIMIENTOTRABAJADOR",
        "ROLTRABAJADOR",
        "HUELLATRABAJADOR",
        "CONTRASEÑA",
        "ESTADO",
    ]
    for campo in campos_requeridos:
        logger.debug(f"Existe el campo: {campo}")
        assert campo in trabajador, f"Falta el campo obligatorio '{campo}' en la respuesta"
    logger.info("Test completado.")
