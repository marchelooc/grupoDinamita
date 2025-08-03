import requests
import pytest
import random
from src.utils.generador_codigo import generar_nombre, generar_codigo_trab, generar_fecha_nac, generar_contraseña
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema

@pytest.mark.smoke
def test_crear_un_trabajador_con_todos_los_datos_validos (get_url):
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
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json")) #schema de entrada

    url_final = get_url + endpoint
    response = requests.post(url_final, json=payload)
    assert response.status_code == 201
    
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json")) #schema de salida             #Crear trabajador por primera vez

    nombre_2 = generar_nombre()
    payload_duplicado = {
        **payload,
        "NOMBRETRABAJADOR": nombre_2, 
        "CONTRASEÑA": generar_contraseña(),    
        "FECHANACIMIENTOTRABAJADOR": generar_fecha_nac()
    }

    response2 = requests.post(url_final, json=payload_duplicado)        #Intentar crear otro trabajador con el mismo código
    assert response2.status_code == 409         # Validación esperada: código duplicado debe ser rechazado"""
