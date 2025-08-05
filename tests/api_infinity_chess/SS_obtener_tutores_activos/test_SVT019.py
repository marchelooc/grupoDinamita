import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG001: Se devuelve una lista vacia cuando se busca un id invalido.", run=True)
def test_obtener_un_trabajador_con_código_de_trabajador_inválido (get_url):
    CODTRABAJADOR = "20300105XYZ@@"
    logger.debug(f"Trabajador buscado: {CODTRABAJADOR}.")
    endpoint = "obtenerTrabajador/" + CODTRABAJADOR
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404 #El codigo no existe, por lo que no debe mostrar nada
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_obtener_trabajador.json")) #schema de salida
    logger.info("Test completado.")