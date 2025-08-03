import requests
import pytest

from src.assertions.add import assert_validarResponseSchema,assert_validarSchemaInput
from src.utils.generadorCodigo import generarNomMateria
from src.utils.cargarSchema import cargar_schema

@pytest.mark.smoke
def test_validar_comportamiento_al_agregar_curso_sin_CODCURSO(get_url):
    nombreMateria = generarNomMateria()
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": "",
                "CURSO": nombreMateria, 
                "ESTADO": "activo",
                }
    assert_validarSchemaInput(payload,cargar_schema("schema_materia.json"))
    urlFinal = get_url + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 500
    