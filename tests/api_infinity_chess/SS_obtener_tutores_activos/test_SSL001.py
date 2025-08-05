import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_obtener_lista_de_tutores_activos_correctamente(get_url):
    logger.info("Iniciando test SSL001.")
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET a {lista_url}.")
    response = requests.get(lista_url)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_obtener_trabajador.json"))
    trabajador = response.json()
    if isinstance(trabajador, list):
        assert trabajador, "La lista contiene los datos del trabajador"
        trabajador = trabajador[0]
    nombre = trabajador.get("NOMBRETRABAJADOR")
    codigo = trabajador.get("CODTRABAJADOR")
    fecha_nac = trabajador.get("FECHANACIMIENTOTRABAJADOR")
    rol = trabajador.get("ROLTRABAJADOR")
    logger.info(f"Detalles del trabajador recuperado:")
    logger.info(f"Nombre: {nombre}")
    logger.info(f"Codigo: {codigo}")
    logger.info(f"Fecha de nacimiento: {fecha_nac}")
    logger.info(f"Rol: {rol}")
    logger.info("Test completado.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    lista_tutores = response.json()
    logger.debug(lista_tutores)
    logger.info("Validando lista tutores activos.")
    for tutor in lista_tutores:
        assert tutor.get("ESTADO") == "Activo", f"Tutor inactivo encontrado: {tutor}"
    logger.info("Test completado.")
