import requests
import pytest
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_contraseña, generar_fecha_nac
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SVBUG008: El sistema no valida el campo NOMBRETRABAJADOR", run=True)
def test_crear_trabajador_con_numeros_en_el_campo_nombre (get_url):
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre)
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    endpoint = "agregarTrabajador"
    payload = {
        "CODTRABAJADOR": codigo,
        "NOMBRETRABAJADOR": "123456SAI",
        "FECHANACIMIENTOTRABAJADOR": fecha,
        "ROLTRABAJADOR": "Maestro",
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": contra,
    }
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final}")
    logger.debug(payload)
    response = requests.post(url_final, json=payload)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 422
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    
    url_delete = f"{get_url}eliminarTrabajador/{codigo}"
    logger.info(f"Enviando DELETE a {url_delete}")
    response_delete = requests.delete(url_delete)
    logger.info(f"Codigo de respuesta DELETE: {response_delete.status_code}")
    assert response_delete.status_code == 200, (f"Codigo de respuesta {response_delete.status_code}")
    logger.info("Test completado.")