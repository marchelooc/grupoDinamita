import requests
import pytest

@pytest.mark.smoke
def test_validarSEDEvacíaRetornaListaVacía(getUrl):
    endpoint = "obtenerEstudiantes/Modulo 4"
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    assert response.status_code == 200
    listaEstudiantes = response.json()
    assert len (listaEstudiantes) > 0