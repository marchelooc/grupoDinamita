import requests
import pytest

from src.assertions.add import assert_validarResponseSchema,assert_validarSchemaInput
from src.utils.generadorCodigo import generarNomMateria, generarCod
from src.utils.cargarSchema import cargar_schema

@pytest.mark.smoke
def test_ValidarComportamientoAlAgregarCursoSinCampoCURSO(getUrl):
    nombreMateria = generarNomMateria()
    codigoMateria = generarCod(nombreMateria)
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": codigoMateria,
                "CURSO": "", 
                "ESTADO": "activo",
                }
    assert_validarSchemaInput(payload,cargar_schema("schemaMateria.json"))
    urlFinal = getUrl + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 500
    assert_validarResponseSchema(response,cargar_schema("schemaMateria.json")) 
    