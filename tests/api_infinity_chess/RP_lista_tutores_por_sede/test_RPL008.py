import requests
import pytest

@pytest.mark.smoke
def test_RPL008_obtener_tutor_por_sede_valida (get_url):
    endpoint = "obtenerTutores/Modulo 4"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200
    lista_tutores = response.json()
    assert len (lista_tutores) > 0
