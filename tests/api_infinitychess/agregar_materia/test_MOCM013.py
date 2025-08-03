import requests
import pytest

from src.assertions.add import assert_validarResponseSchema,assert_validarSchemaInput
from src.utils.generadorCodigo import generarNomMateria, generarCod
from src.utils.cargarSchema import cargar_schema

@pytest.mark.smoke
def test_validar_el_limite_maximo_de_caracteres_del_campo_CODCURSO(get_url):
    nombreMateria = generarNomMateria()
    codigoMateria = generarCod(nombreMateria)
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": codigoMateria + "123456789",
                "CURSO": nombreMateria, 
                "ESTADO": "activo",
                }
    assert_validarSchemaInput(payload,cargar_schema("schema_materia.json"))
    urlFinal = get_url + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 500

    