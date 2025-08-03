import requests
import pytest

from src.assertions.add import assert_validarResponseSchema,assert_validarSchemaInput
from src.utils.generadorCodigo import generarNomMateria, generarCod
from src.utils.cargarSchema import cargar_schema

@pytest.mark.smoke
def test_agregar_una_materia_con_datos_válidos(get_url):
    nombreMateria = generarNomMateria()
    codigoMateria = generarCod(nombreMateria)
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": codigoMateria,
                "CURSO": nombreMateria, 
                "ESTADO": "activo",
                }
    assert_validarSchemaInput(payload,cargar_schema("schema_materia.json"))
    urlFinal = get_url + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 201
    assert_validarResponseSchema(response,cargar_schema("schema_materia.json")) 
    