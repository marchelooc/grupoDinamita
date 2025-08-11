import requests
from src.utils.logger_config import logger 

def obtener_estudiantes(get_url):
    endpoint = "obtenerEstudiantes/Quillacollo"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_estudiantes = response.json()
    return lista_estudiantes

def obtener_tutores_inactivos(get_url):
    endpoint = "obtenerTutoresInactivos"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_tutores = response.json()
    return lista_tutores

def enviar_solicitud(get_url,codigo_estudiante ,headers=None):
    endpoint = "obtenerHorarioEstudiante/"+ codigo_estudiante
    lista_url = get_url + endpoint
    logger.info(f"Enviando PUT a {lista_url}.")
    return requests.get(lista_url, headers=headers)

def verificar_horarios(lista_horarios):
    if (len(lista_horarios) > 0): 
        for horario in lista_horarios:
            assert "CODESTUDIANTE" in horario, f"Falta 'CODESTUDIANTE' en: {horario}"
            assert "CODCURSOINSCRITO" in horario, f"Falta 'CODCURSOINSCRITO' en: {horario}"
            assert "CODGRUPOINSCRITO" in horario, f"Falta 'CODGRUPOINSCRITO' en: {horario}"
            assert "NOMBREGRUPO" in horario, f"Falta 'NOMBREGRUPO' en: {horario}"
            assert "DIA" in horario, f"Falta 'DIA' en: {horario}"
            assert "HORA" in horario, f"Falta 'HORA' en: {horario}"
        logger.info("Horarios obtenidos validados correctamente.")
    else:
        logger.debug("El estudiante no cuenta con horarios.")

def verificar_estructura_horario (lista_horarios):
    estructura_horario = { "CODESTUDIANTE","CODCURSOINSCRITO","CODGRUPOINSCRITO","NOMBREGRUPO","DIA","HORA"}
    for horario in lista_horarios:
        campos_horario = set(horario.keys())
        campos_faltan = estructura_horario - campos_horario
        assert not campos_faltan , f"CamposFaltantes: {campos_faltan} del horario {horario}"
    logger.info("Estructura validada correctamente.")
