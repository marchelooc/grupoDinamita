import requests
import pytest
from datetime import datetime, timedelta
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_contraseña, generar_fecha_mayor
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG006: El estatus code mostrado es 201, cuando debe ser 422", run=False)
def test_crear_trabajador_mayor_de_75_años (get_url):
    # Datos válidos
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    contra = generar_contraseña()
    fecha = generar_fecha_mayor()
    endpoint = "agregarTrabajador"
    payload = {
        "CODTRABAJADOR": codigo,
        "NOMBRETRABAJADOR": nombre,
        "FECHANACIMIENTOTRABAJADOR": fecha,
        "ROLTRABAJADOR": "Maestro",
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": contra,
    }
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json")) 
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final}")
    response = requests.post(url_final, json=payload)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 422      # El trabajador es mayor de 75 años, dato invalido
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json")) 
    logger.info("Test completado.")