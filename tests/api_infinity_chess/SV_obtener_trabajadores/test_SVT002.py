import pytest
from src.utils.generador_codigo import generar_codigo
from src.api_infinity_chess.obtener_trabajadores import enviar_GET
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG001: Se devuelve un codigo 200 con una lista vacía cuando se busca un id inexistente", run=True)
def test_obtener_trabajador_con_Id_inexistente(get_url):
    logger.info("Inicio de test SVT002.")
    logger.info("Generar codigo inexistente.")
    CODTRABAJADOR = generar_codigo()
    logger.debug(f"Trabajador elegido: {CODTRABAJADOR}.")
    response = enviar_GET (get_url, CODTRABAJADOR)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404 #El codigo no existe, por lo que debe mostrar error 404
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_obtener_trabajador.json"))
    logger.info("Test completado.")