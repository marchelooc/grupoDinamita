import requests
import pytest
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac, generar_contraseña
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG003: El estatus code mostrado es 500, cuando debe ser 409", run=False)
def test_crear_un_trabajador_con_un_codigo_que_ya_existe (get_url):
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    endpoint = "agregarTrabajador"
    payload = {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final}")
    response = requests.post(url_final, json=payload)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 201
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))

    nombre_2 = generar_nombre()
    payload_duplicado = {
        **payload,
        "NOMBRETRABAJADOR": nombre_2, 
        "CONTRASEÑA": generar_contraseña(),    
        "FECHANACIMIENTOTRABAJADOR": generar_fecha_nac()
    }
    logger.info("Intentando crear un trabajador con un código ya existente.")
    logger.debug(f"Payload duplicado: {payload_duplicado!r}")
    response2 = requests.post(url_final, json=payload_duplicado)
    logger.info(f"Código de respuesta al intento duplicado: {response2.status_code}")
    assert response2.status_code == 409         # código duplicado debe ser rechazado
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    logger.info("Test completado.")
