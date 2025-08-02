import requests
import pytest
import random
from src.utils.generadorCodigo import generarNombre, generarCodigoTrab, generarFechaNac, generarContraseña
from src.assertions.add import assert_validarResponseSchema
from src.utils.cargarSchema import cargar_schema

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
    
    assert_validarResponseSchema(response,cargar_schema("schemaTrabajador.json"))