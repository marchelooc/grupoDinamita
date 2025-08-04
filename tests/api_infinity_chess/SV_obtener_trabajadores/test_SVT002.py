import requests
import pytest
from src.utils.generador_codigo import generar_codigo
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
def test_obtener_trabajador_con_Id_inexistente(get_url):
    CODTRABAJADOR = generar_codigo()
    logger.debug(f"Trabajador buscado: {CODTRABAJADOR}.")
    endpoint = "obtenerTrabajador/" + CODTRABAJADOR
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 404 #El codigo no existe, por lo que no debe mostrar nada
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_obtener_trabajador.json")) #schema de salida
    logger.info("Test completado.")