import requests
import pytest
from src.assertions.add import assert_validarResponseSchema,assert_validarSchemaInput
from src.utils.cargarSchema import cargar_schema
from src.api_infinityChess.obtenerCurso import obtenerCursos

@pytest.mark.smoke
def test_ValidarComportamientoAlAgregarCursoConCODCURSOduplicado(getUrl):
    endpoint = "agregarCurso"

    payload = {
                "CODCURSO": "123Mrepetida",
                "CURSO": "MateriaRepetida", 
                "ESTADO": "activo",
                }
    if not existeMateriaRepetida(getUrl):
        response_crear = requests.post(urlFinal, json=payload)
        assert response_crear.status_code == 201
        
    assert_validarSchemaInput(payload,cargar_schema("schemaMateria.json"))
    urlFinal = getUrl + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 500
    assert_validarResponseSchema(response,cargar_schema("schemaMateria.json")) 
    

def existeMateriaRepetida(getUrl) -> bool:
    nombre_materia_buscada = "MateriaRepetida"
    listaMaterias = obtenerCursos(getUrl)
    return any(m["CURSO"] == nombre_materia_buscada for m in listaMaterias)
