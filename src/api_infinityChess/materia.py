from src.api_infinityChess.obtenerCurso import obtenerCursos
import requests

def existeMateriaRepetida(getUrl) -> bool:
    nombre_materia_buscada = "MateriaRepetida"
    listaMaterias = obtenerCursos(getUrl)
    return any(m["CURSO"] == nombre_materia_buscada for m in listaMaterias)

def crear_materia_repetida(getUrl, endpoint):
    payload = {
                "CODCURSO": "123Mrepetida",
                "CURSO": "MateriaRepetida",
                "ESTADO": "activo",
                }
    urlFinal = getUrl + endpoint
    response_crear = requests.post(urlFinal, json=payload)
    assert response_crear.status_code == 201