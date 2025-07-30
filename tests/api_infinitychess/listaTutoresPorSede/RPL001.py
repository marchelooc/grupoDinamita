import requests
import pytest

@pytest.mark.smoke
def test_RPL001_obtenerTutorPorSedeValida (getUrl):
    endpoint = "obtenerTutores/Modulo 4"
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200
    listaTutores = response.json()
    assert len (listaTutores) > 0
