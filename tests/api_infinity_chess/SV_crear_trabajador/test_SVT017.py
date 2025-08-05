import requests
import pytest
import json
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac, generar_contraseña
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG011: El estatus code mostrado es 500, cuando debe ser 415", run=False)
def test_crear_un_trabajador_con_content_type_text_plain (get_url):
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre).strip()
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    endpoint = "agregarTrabajador"
    url_final = get_url + endpoint
    payload = {
        "CODTRABAJADOR": codigo,
        "NOMBRETRABAJADOR": nombre,
        "FECHANACIMIENTOTRABAJADOR": fecha,
        "ROLTRABAJADOR": "Maestro",
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": contra,
    }
    headers = {"Content-Type": "text/plain"} # Se envia el mismo payload con Content-Type: text/plain
    body = json.dumps(payload)

    logger.info(f"Enviando POST a {url_final} con Content-Type text/plain")
    logger.debug(f"Body (text/plain): {body}")
    response = requests.post(url_final, data=body, headers=headers)
    logger.info(f"Código de respuesta: {response.status_code}")
    assert response.status_code == 415
    logger.info("Test completado.")