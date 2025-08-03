import requests
import pytest
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.validation
def test_crear_trabajador_con_contrasena_menor_8_caracteres(get_url):
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre)
    fecha = generar_fecha_nac()
    contra_corta = "Abc123"        # Contraseña intencionalmente corta

    endpoint = "agregarTrabajador"
    payload = {
        "CODTRABAJADOR": codigo,
        "NOMBRETRABAJADOR": nombre,
        "FECHANACIMIENTOTRABAJADOR": fecha,
        "ROLTRABAJADOR": "Maestro",
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": contra_corta,
    }

    url_final = get_url + endpoint
    response = requests.post(url_final, json=payload)
    assert response.status_code == 422

    # Si existe un esquema de error para validaciones de payload:
    assert_validar_response_schema(response, cargar_schema("schema_error.json"))