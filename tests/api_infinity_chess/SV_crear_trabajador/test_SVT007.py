import requests
import pytest
import random
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac, generar_contraseña
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajador_por_Id

@pytest.mark.funcional
def test_Verificar_que_el_trabajador_creado_exista_en_el_sistema (get_url):
    nombre = generar_nombre()
    codigo = generar_codigo_trab(nombre)
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
    urlFinal = get_url + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 201
    
    Trabajador = obtener_trabajador_por_Id(get_url,codigo)
    assert len(Trabajador) > 0