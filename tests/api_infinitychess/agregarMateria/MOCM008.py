#Agregar una materia con datos válidos
#import requests
#import json
#url = "https://backend.clubinfinitychess.com/agregarCurso"
#payload = json.dumps({
#  "CODCURSO": "2025PyTest",
#  "CURSO": "PythonTest"
#})
#headers = {
#  'Content-Type': 'application/json',
#  'Cookie': 'XSRF-TOKEN=eyJpdiI6ImQwK0VERnB2K28yUzFWNzFQWmI0WkE9PSIsInZhbHVlIjoic25XZFhubGdiYnQ5d2ZMak12eWRaUlZrMUhIaW5Ka1MyZUV6QmxLaWxvc0Uxb2Q1dW11WXhJcXBEVjN4RnE1VWxNaDRldUQ5UFB0dXB6akwxZm5vZ3ZKdjg3ckFNZm8ya1dXSVNJbkdpd1lJWXFab291czhMTmhNaEtnL0NDUGkiLCJtYWMiOiJjOGRlOTliNDBkZjI1M2ExNDY0Mjk4MGE4ZTIzZGE2ZmQ2MWFlZDBkNTNlZDQwZTI5MTk3ZDVlMjZiYzYwM2ZmIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IlV6K1B5RnAxckZ6cFZCU240Q0lvQWc9PSIsInZhbHVlIjoiWVFMRzFkQkdmNEg2NkZFRkhsMjZwcVNTbjJnVW0rc1pXRzVaei9nSEdmeWx4NCt1QlFoR2hoK2tqcUlSWC9UR3VRQmlDTHd6QWNleUNpdW1oTGQwUDFOT011bkNJRHZDTVZBZW5ZZGdlRUpBSVdVdlpoRUNEek1QMWdyaElVZVYiLCJtYWMiOiJkMTcwZmE3ODNiM2Q5NWVmODFmNDhkZDRjNzYzZWE1Zjk3MGEyZTc2Njc1YjVmNjI3ZWMxNzE5YTFjMGUwNGM5IiwidGFnIjoiIn0%3D'
#}
#response = requests.request("POST", url, headers=headers, data=payload)
#print(response.text)
import requests
import pytest


from src.generadorCodigo import generarNomMateria, generarCod
@pytest.mark.smoke
def test_AgregarUnaMateriaConDatosVálidos(getUrl):
    nombreMateria = generarNomMateria()
    codigoMateria = generarCod(nombreMateria)
    endpoint = "agregarCurso"
    payload = {
                "CODCURSO": codigoMateria,
                "CURSO": nombreMateria, 
                "ESTADO": "activo",
                }
    urlFinal = getUrl + endpoint
    response = requests.post(urlFinal, json=payload)
    print(f"Materia creada es: {nombreMateria}")
    assert response.status_code == 201



