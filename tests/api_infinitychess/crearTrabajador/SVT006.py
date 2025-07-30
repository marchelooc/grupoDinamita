import requests
import pytest
import random
from src.generadorCodigo import generarNombre, generarCodigoTrab, generarFechaNac, generarContraseña
@pytest.mark.smoke
def test_cambioDeEstadoDeTutorActivo (getUrl):
    nombre = generarNombre()
    codigo = generarCodigoTrab(nombre)
    fecha = generarFechaNac()
    contra = generarContraseña()
    endpoint = "agregarTrabajador"
    payload = {
                "CODTRABAJADOR": codigo,
                "NOMBRETRABAJADOR": nombre, 
                "FECHANACIMIENTOTRABAJADOR": fecha, 
                "ROLTRABAJADOR" : "Maestro",
                "CODSEDE": "Modulo 4",
                "CONTRASEÑA": contra,
                }
    urlFinal = getUrl + endpoint
    response = requests.post(urlFinal, json=payload)
    assert response.status_code == 201