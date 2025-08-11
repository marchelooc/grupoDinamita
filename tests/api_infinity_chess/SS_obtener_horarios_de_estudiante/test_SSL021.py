import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_estudiantes import enviar_solicitud, verificar_horarios
from src.api_infinity_chess.cambiar_estado_estudiante import obtener_estudiante_aleatorio

@pytest.mark.functional
def test_solicitud_sin_headers(get_url):
    logger.info("Iniciando test SSL021.")
    headers = {
    }
    logger.info("Obtener un estudiante aleatorio.")
    cod_estudiante = obtener_estudiante_aleatorio (get_url)
    logger.debug(f"Estudiante seleccionado: {cod_estudiante}.")
    response = enviar_solicitud(get_url,cod_estudiante,headers)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.debug(f"Response: {response.json()}")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_horario_estudiante.json"))
    lista_horarios = response.json()
    logger.info("Validando lista horarios.")
    verificar_horarios(lista_horarios)
    logger.info("Test completado.")
    
    
    