import requests
import pytest
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac, generar_contraseña
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.validation
def test_crear_trabajador_con_campos_vacios(get_url):
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre)
    fecha = generar_fecha_nac()
    endpoint = "agregarTrabajador"
    payload = {
        "CODTRABAJADOR": codigo,
        "NOMBRETRABAJADOR": "",               # Campo vacío
        "FECHANACIMIENTOTRABAJADOR": fecha,
        "ROLTRABAJADOR": "Maestro",
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": "",                     # Campo vacío
    }

    url_final = get_url + endpoint
    response = requests.post(url_final, json=payload)
    assert response.status_code == 422         # La API debe rechazar payloads con campos vacíos

    # Si existe un schema de errores definido:
    assert_validar_response_schema(response, cargar_schema("schema_error.json"))
