import requests
import pytest
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac, generar_contraseña
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajador_por_Id
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.funcional
def test_Verificar_que_el_trabajador_creado_exista_en_el_sistema (get_url):
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
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json")) #schema de entrada
    url_final = get_url + endpoint
    logger.info(f"Enviando POST a {url_final} con payload: {payload}")
    response = requests.post(url_final, json=payload, verify=False)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 201
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json")) #schema de salida
    logger.info("Test completado.")
    
    logger.info("Obteniendo el trabajador recién creado por ID para verificar existencia.")
    Trabajador = obtener_trabajador_por_Id(get_url,codigo)
    logger.debug(f"Respuesta de obtener_trabajador_por_Id: {Trabajador!r}")
    assert len(Trabajador) > 0
    logger.info("Test completado.")