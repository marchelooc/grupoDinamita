import requests
import pytest
import random

from src.assertions.add import assert_crearGrupoSchema
from src.obtenerCurso import obtenerCursos
from src.generadorCodigo import generarCod, obtenerDias, obtenerHoras, obtenerLimite, obtenerPrecio

@pytest.mark.smoke
def test_AgregarUnNuevoGrupoCon40CaracteresEnNombre(getUrl):
    listaCursos = obtenerCursos(getUrl)
    CODCURSO = random.choice(listaCursos)["CODCURSO"]
    print(f"Curso seleccionado: {CODCURSO}")
    endpoint = "agregarGrupo"
    NombreGrupo="Este es el nombre de grupo con muy largo"
    Dias=obtenerDias()
    horas=obtenerHoras()
    precio=obtenerPrecio()
    limite=obtenerLimite()
    codigo=generarCod(NombreGrupo)

    payload = {
        "CODCURSO": CODCURSO,
        "CODSEDE": "Modulo 4",
        "NOMBREGRUPO": NombreGrupo, 
        "CODGRUPO": codigo,
        "LIMITE" :limite,
        "PRECIO":precio,
        "DIAS" : Dias,
        "HORA":horas} 
    
    urlFinal = getUrl + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 201
    assert_crearGrupoSchema(response)