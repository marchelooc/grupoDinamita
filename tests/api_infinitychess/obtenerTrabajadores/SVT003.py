import requests
import pytest

@pytest.mark.exploratory
def test_obtenerTrabajadorSinEnviarId(getUrl):
    endpoint = "obtenerTrabajadores/"
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 404