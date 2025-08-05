import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

<<<<<<< HEAD:tests/api_infinity_chess/SV_obtener_trabajadores/test_SVT002.py
@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG001: Se devuelve una lista vacía cuando se busca un id inexistente", run=True)
def test_obtener_trabajador_con_Id_inexistente(get_url):
    CODTRABAJADOR = generar_codigo()
    logger.debug(f"Trabajador buscado: {CODTRABAJADOR}.")
    endpoint = "obtenerTrabajador/" + CODTRABAJADOR
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404 #El codigo no existe, por lo que no debe mostrar nada
=======
@pytest.mark.functional
def test_verificación_del_código_de_respuesta(get_url):
    logger.info("Iniciando test SSL004.")
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    lista_tutores = response.json()
    logger.debug(lista_tutores)
>>>>>>> 818bf39e2e9685a9c75e5faa347ab9253cecefaa:tests/api_infinity_chess/SS_obtener_tutores_activos/test_SSL004.py
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    logger.info("Test completado.")
