import requests
import pytest
import jsonschema


from src.assertions.addMateria import assert_crearMateriaSchema 
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
    assert_crearMateriaSchema(response) 
    
