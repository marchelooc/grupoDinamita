import requests
import pytest
import random
from src.utils.generador_codigo import generar_codigo

@pytest.mark.negative
def test_obtener_trabajador_con_Id_inexistente(get_url):
    CODTRABAJADOR = generar_codigo()
    print(f"Trabajador escogido es: {CODTRABAJADOR}")
    endpoint = "obtenerTrabajadores/" + CODTRABAJADOR
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 404