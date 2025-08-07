import requests
from src.utils.logger_config import logger 

def obtener_tutores_activos(get_url):
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_tutores = response.json()
    return lista_tutores

def obtener_tutores_inactivos(get_url):
    endpoint = "obtenerTutoresInactivos"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_tutores = response.json()
    return lista_tutores

def enviarSolicitud(get_url, headers=None):
    endpoint = "obtenerTutoresActivos"
    lista_url = get_url + endpoint
    logger.info(f"Enviando PUT a {lista_url}.")
    return requests.get(lista_url, headers=headers)

def verificar_tutores_activos (lista_tutores):
    for tutor in lista_tutores:
        assert tutor.get("ESTADO") == "Activo", f"Tutor inactivo encontrado: {tutor}"
    logger.info("Test completado.")
    
def verificar_estructura_tutores (lista_tutores):
    estructura_tutor = {"CODTUTOR","NOMBRETUTOR","APELLIDOTUTOR","FECHANACIMIENTOTUTOR","CELULARTUTOR","GENEROTUTOR", "OCUPACION", "CORREO", "ESTADO","CELULARALTERNATIVO"}
    for tutor in lista_tutores:
        campos_tutor = set(tutor.keys())
        campos_faltan = estructura_tutor - campos_tutor
        assert not campos_faltan , f"CamposFaltantes: {campos_faltan} del tutor {tutor}"
