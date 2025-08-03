import requests
import pytest
from datetime import datetime, timedelta
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_contraseña, generar_fecha_mayor

@pytest.mark.negative
def test_crear_trabajador_menor_de_edad(get_url):
    # Datos válidos
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre)
    contra = generar_contraseña()
    fecha = generar_fecha_mayor()

    payload = {
        "CODTRABAJADOR": codigo,
        "NOMBRETRABAJADOR": nombre,
        "FECHANACIMIENTOTRABAJADOR": fecha,
        "ROLTRABAJADOR": "Maestro",
        "CODSEDE": "Modulo 4",
        "CONTRASEÑA": contra,
    }

    url_final = get_url + "agregarTrabajador"
    response = requests.post(url_final, json=payload)
    assert response.status_code == 422      # Se espera que falle porque el trabajador es mayor de 75 años
    