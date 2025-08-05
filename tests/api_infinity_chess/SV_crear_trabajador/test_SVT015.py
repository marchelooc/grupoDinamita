import requests
import pytest
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_contraseña
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_crear_trabajador_con_campos_vacios (get_url):
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre)
    contra = generar_contraseña()
    endpoint = "agregarTrabajador"
    payload = {
        "CODTRABAJADOR": codigo,
        "NOMBRETRABAJADOR": nombre,
        "FECHANACIMIENTOTRABAJADOR": "",        #campo vacio
        "ROLTRABAJADOR": "",        #campo vacio
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": contra,
    }
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final}")
    logger.debug(payload)
    response = requests.post(url_final, json=payload)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 201
    
    url_delete = f"{get_url}eliminarTrabajador/{codigo}"
    logger.info(f"Enviando DELETE a {url_delete}")
    response_delete = requests.delete(url_delete)
    logger.info(f"Codigo de respuesta DELETE: {response_delete.status_code}")
    assert response_delete.status_code == 200, (f"Codigo de respuesta {response_delete.status_code}")
    logger.info("Test completado.")
    