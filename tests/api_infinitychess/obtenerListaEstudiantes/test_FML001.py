import requests
import pytest

@pytest.mark.smoke
def test_validarSEDEvacíaRetornaListaVacía(getUrl):
    endpoint = "obtenerEstudiantes/"
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 404