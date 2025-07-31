import requests
import pytest
import random
from src.generadorCodigo import generarCodigo

@pytest.mark.negative
def test_obtenerTrabajadorConIdInexistente(getUrl):
    CODTRABAJADOR = generarCodigo()
    print(f"Trabajador escogido es: {CODTRABAJADOR}")
    endpoint = "obtenerTrabajadores/" + CODTRABAJADOR
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 404