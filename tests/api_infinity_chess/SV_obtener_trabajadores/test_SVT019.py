import pytest
from src.api_infinity_chess.obtener_trabajadores import enviar_GET, obtener_codigo_de_trabajador_invalido
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG001: Se devuelve un codigo 200 con una lista vacia cuando se busca un id invalido.", run=True)
def test_obtener_un_trabajador_con_código_de_trabajador_inválido (get_url):
    logger.info("Inicio de test SVT019.")
    response = enviar_GET (get_url, obtener_codigo_de_trabajador_invalido())
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404 #El codigo no existe, por lo que debe mostrar error 404
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_obtener_trabajador.json"))
    logger.info("Test completado.") 