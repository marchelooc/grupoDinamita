import requests
import pytest
from src.utils.generadorCodigo import generarNomMateria, generarCod

@pytest.mark.smoke
def test_AgregarUnaMateriaConDatosVálidos(getUrl):
    nombreMateria = generarNomMateria()
    codigoMateria = generarCod(nombreMateria)
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": codigoMateria,
                "CURSO": nombreMateria, 
                "ESTADO": "activo",
                }
    urlFinal = getUrl + endpoint
    response = requests.post(urlFinal, json=payload)
    print(f"Materia creada es: {nombreMateria}")
    assert response.status_code == 201



