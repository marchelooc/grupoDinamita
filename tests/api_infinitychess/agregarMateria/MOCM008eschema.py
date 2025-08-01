import requests
import pytest

from src.assertions.add import assert_validarResponseSchema
from src.utils.generadorCodigo import generarNomMateria, generarCod
from utils.cargarSchema import cargar_schema

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
    assert_validarResponseSchema(response,cargar_schema("schemaMateria.json")) 
    
