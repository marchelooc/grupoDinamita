import requests

def obtenerMateria(getUrl):
    #esta variable tengo q modificar sergio culon
    curso = "CANTO"
    endpoint = "verificarCurso/" + curso
    lista_url = getUrl + endpoint
    response = requests.get(lista_url)
    listaMaterias = response.json()
    return listaMaterias
