import requests
import pytest
import random

from src.assertions.add import assert_crearGrupoSchema
from src.obtenerCurso import obtenerCursos
from src.generadorCodigo import obtenerNombreGrupo, generarCod, obtenerDias, obtenerHoras, obtenerPrecio

@pytest.mark.negative
def test_AgregarUnNuevoGrupoConLimiteCero(getUrl):
    listaCursos = obtenerCursos(getUrl)
    CODCURSO = random.choice(listaCursos)["CODCURSO"]
    print(f"Curso seleccionado: {CODCURSO}")
    endpoint = "agregarGrupo"
    NombreGrupo=obtenerNombreGrupo()
    Dias=obtenerDias()
    horas=obtenerHoras()
    precio=obtenerPrecio()
    limite=0
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
    assert response.status_code == 400
    assert_crearGrupoSchema(response)