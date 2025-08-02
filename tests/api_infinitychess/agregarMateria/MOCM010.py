import requests
import pytest

from src.assertions.add import assert_validarResponseSchema,assert_validarSchemaInput
from src.utils.generadorCodigo import generarNomMateria
from src.utils.cargarSchema import cargar_schema

@pytest.mark.smoke
def test_ValidarComportamientoAlAgregarCursoSinCODCURSO(getUrl):
    nombreMateria = generarNomMateria()
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": "",
                "CURSO": nombreMateria, 
                "ESTADO": "activo",
                }
    assert_validarSchemaInput(payload,cargar_schema("schemaMateria.json"))
    urlFinal = getUrl + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 500
    assert_validarResponseSchema(response,cargar_schema("schemaMateria.json")) 
    