import requests
import pytest
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac, generar_contraseña
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajador_por_Id
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.regression
def test_verificar_los_datos_del_trabajador_creado (get_url):
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    rol = "Maestro"
    sede = "Modulo 4"
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
    logger.debug(payload)
    response = requests.post(url_final, json=payload)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 201
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    
    url_get = f"{get_url}obtenerTrabajador/{codigo}"
    logger.info(f"Enviando GET a {url_get}")
    response_get = requests.get(url_get)
    logger.info(f"Codigo de respuesta GET: {response_get.status_code}")
    assert response_get.status_code == 200, f"Codigo de respuesta {response_get.status_code}"
    logger.info("Validando schema de la respuesta GET.")
    assert_validar_response_schema(response_get, cargar_schema("schema_obtener_trabajador.json"))
    
    trabajador = response_get.json()
    if isinstance(trabajador, list):
        assert trabajador, "La lista contiene los datos del trabajador"
        trabajador = trabajador[0]
    logger.debug(f"Datos del trabajador recuperado: {trabajador!r}")
    logger.info(f"Codigo: {codigo}")
    assert trabajador["CODTRABAJADOR"] == codigo
    logger.info(f"Nombre: {nombre}")
    assert trabajador["NOMBRETRABAJADOR"] == nombre
    logger.info(f"Fecha de nacimiento: {fecha}")
    assert trabajador["FECHANACIMIENTOTRABAJADOR"] == fecha
    logger.info(f"Rol: {rol}")
    assert trabajador["ROLTRABAJADOR"] == rol
    if "CODSEDE" in trabajador:
        logger.info(f"Sede:{sede}")
        assert trabajador["CODSEDE"] == sede
    
    url_delete = f"{get_url}eliminarTrabajador/{codigo}"
    logger.info(f"Enviando DELETE a {url_delete}")
    response_delete = requests.delete(url_delete)
    logger.info(f"Codigo de respuesta DELETE: {response_delete.status_code}")
    assert response_delete.status_code == 200, (f"Codigo de respuesta {response_delete.status_code}")
    logger.info("Test completado.")