import requests
import pytest
import random
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajadores

@pytest.mark.smoke
def test_validar_que_la_contraseña_se_muestre_cifrada(get_url):
    lista_trabajdores = obtener_trabajadores(get_url)
    CODTRABAJADOR = random.choice(lista_trabajdores)["CODTRABAJADOR"]
    print(f"Trabajador escogido es: {CODTRABAJADOR}")
    endpoint = "obtenerTrabajadores/" + CODTRABAJADOR
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200
    trabajador = response.json()
    for trab in trabajador:
        assert len(trab.get("CONTRASEÑA")) > 30