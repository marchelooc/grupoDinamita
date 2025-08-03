import requests
import pytest

from src.assertions.add import assert_validarResponseSchema,assert_validarSchemaInput
from src.utils.generadorCodigo import generarNomMateria, generarCod
from src.utils.cargarSchema import cargar_schema

@pytest.mark.funcional
def test_validar_comportamiento_al_agregar_un_curso_con_todos_los_campos_vacíos(get_url):
    nombreMateria = generarNomMateria()
    codigoMateria = generarCod(nombreMateria)
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": "",
                "CURSO": "",
                "ESTADO": "",
                }
    assert_validarSchemaInput(payload,cargar_schema("schema_materia.json"))
    urlFinal = get_url + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 500
    