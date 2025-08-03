import requests
import pytest
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac, generar_contraseña
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.regression
def test_crear_trabajador_con_rol_invalido(get_url):
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre)
    fecha = generar_fecha_nac()
    contra = generar_contraseña()
    endpoint = "agregarTrabajador"
    payload = {
        "CODTRABAJADOR": codigo,
        "NOMBRETRABAJADOR": nombre,
        "FECHANACIMIENTOTRABAJADOR": fecha,
        "ROLTRABAJADOR": "RolInvalido",  # Valor inválido
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": contra,
    }

    url_final = get_url + endpoint
    response = requests.post(url_final, json=payload)
    assert response.status_code == 422      # Verificar que la API rechaza el rol inválido con código 422

    # Opcional: validar que el mensaje de error mencione el campo 'ROLTRABAJADOR'
    #data = response.json()
    #assert "rol inválido" in data.get("message", "").lower()

    # Si tienes un schema de errores definido, puedes validarlo así:
    assert_validar_response_schema(response, cargar_schema("schema_error.json"))
