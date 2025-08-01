import requests
import pytest
import random
from src.obtenerTrabajadores import obtenerTrabajadores

@pytest.mark.smoke
def test_validarQueLaContraseñaSeMuestreCifrada(getUrl):
    listaTrabajdores = obtenerTrabajadores(getUrl)
    CODTRABAJADOR = random.choice(listaTrabajdores)["CODTRABAJADOR"]
    print(f"Trabajador escogido es: {CODTRABAJADOR}")
    endpoint = "obtenerTrabajadores/" + CODTRABAJADOR
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200
    trabajador = response.json()
    for trab in trabajador:
        assert len(trab.get("CONTRASEÑA")) > 30