import requests
import pytest
import random
from src.api_infinityChess.obtenerTrabajadores import obtenerTrabajadores

@pytest.mark.exploratory
def test_verificarQueLaURLIncorrectaRetorne404(getUrl):
    listaTrabajdores = obtenerTrabajadores(getUrl)
    CODTRABAJADOR = random.choice(listaTrabajdores)["CODTRABAJADOR"]
    print(f"Trabajador escogido es: {CODTRABAJADOR}")
    endpoint = "obtenerTrabajadorees/" + CODTRABAJADOR
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 404