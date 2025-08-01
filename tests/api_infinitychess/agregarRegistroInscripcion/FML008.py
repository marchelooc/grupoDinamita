import requests
import pytest
import random

from src.utils.generadorCodigo import generar_cod_inscripcion, generarNombre, obtenerPrecio
from datetime import date
from src.api_infinityChess.obtenerTrabajadores import obtenerTrabajadores

@pytest.mark.smoke
def test_MostrarMensajeDeExitoAlGuardarRegistroConDatosVálidos(getUrl):
    codigo = generar_cod_inscripcion(generarNombre())
    listaTrabajdores = obtenerTrabajadores(getUrl)
    CODTRABAJADOR = random.choice(listaTrabajdores)["CODTRABAJADOR"]
    costoInscripcion = obtenerPrecio()
    endpoint = "agregarRegistro"
    payload = {
        "CODINSCRIPCION": codigo,
        "CODTRABAJADOR": CODTRABAJADOR,
        "FECHAINSCRIPCION": date.today().strftime("%d/%m/%Y"), 
        "COSTOINSCRIPCION": costoInscripcion,
        "SEDE" : "Modulo 4",
        "HABILITADO": "Activo",} 
    
    urlFinal = getUrl + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 201