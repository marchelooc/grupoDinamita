import requests
import pytest

@pytest.mark.exploratory
def test_obtener_trabajador_sin_enviar_Id(get_url):
    endpoint = "obtenerTrabajadores/"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 404