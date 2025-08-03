import requests
import pytest
import random
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajadores

@pytest.mark.exploratory
def test_verificar_que_la_URL_incorrecta_retorne_error_404(get_url):
    lista_trabajdores = obtener_trabajadores(get_url)
    CODTRABAJADOR = random.choice(lista_trabajdores)["CODTRABAJADOR"]
    print(f"Trabajador escogido es: {CODTRABAJADOR}")
    endpoint = "obtenerTrabajadorees/" + CODTRABAJADOR
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 404