import requests
import pytest
import random
from src.generadorCodigo import generarNombre, generarCodigoTrab, generarFechaNac, generarContraseña
from src.assertions.addtr import assert_crearTrabajadorSchema
@pytest.mark.smoke
def test_crearUnTrabajadorConTodosLosDatosValidos (getUrl):
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
    
    assert_crearTrabajadorSchema(response)