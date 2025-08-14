import random
import requests
from src.api_infinity_chess.obtener_curso import obtener_cursos
from src.utils.payload.generar_payload_grupo import generar_payload_duplicado,generar_payload_eliminar,generar_payload_limite
from src.utils.generador_codigo import obtener_nombre_grupo, generar_cod, obtener_dias, obtener_horas, obtener_limite, obtener_precio
from src.utils.logger_config import logger

def codigo_curso(get_url):
    lista_cursos = obtener_cursos(get_url)
    CODCURSO = random.choice(lista_cursos)["CODCURSO"]
    return CODCURSO

def realizar_peticion(get_url,payload):
    end_point = "agregarGrupo"
    url_final = get_url + end_point
    logger.info(f"Enviando POST a {url_final}.")
    return requests.post(url_final, json=payload)

def crear_grupo_duplicado(get_url,CODCURSO):
    nombre_grupo=obtener_nombre_grupo()
    end_point = "agregarGrupo"
    payload=generar_payload_duplicado(CODCURSO,nombre_grupo)
    url_final = get_url + end_point
    requests.post(url_final, json=payload)
    return nombre_grupo

def solicitar_peticion(get_url,CODMATERIA,headers):
    end_point = "obtenerGrupo/"+CODMATERIA+"/Modulo 4"
    lista_url = get_url + end_point
    logger.info(f"Enviando GET a {lista_url}.")
    return requests.get(lista_url, headers=headers)

def solicitar_peticion_limite(get_url,CODMATERIA,headers):
    end_point = "obtenerGrupoLimite/"+CODMATERIA+"/Modulo 4"
    lista_url = get_url + end_point
    logger.info(f"Enviando GET a {lista_url}.")
    return requests.get(lista_url, headers=headers)



def obtener_lista_grupos(get_url,CODMATERIA):
    endpoint = "obtenerGrupo/"+CODMATERIA+"/Modulo 4"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_grupos = response.json()
    return lista_grupos

def crear_grupo(get_url,CODCURSO):
    end_point = "agregarGrupo"
    nombre_grupo=obtener_nombre_grupo()
    codigo=generar_cod(nombre_grupo)
    payload=generar_payload_eliminar(CODCURSO,nombre_grupo,codigo)
    logger.debug(f"payload generado: {payload}")
    url_final = get_url + end_point
    requests.post(url_final, json=payload)
    return codigo

def eliminar_grupo(get_url,codigo):
    end_point="/eliminarGrupo/"+codigo
    url_final= get_url + end_point
    return requests.delete(url_final)

def realizar_eliminacion(get_url,codigo,):
    end_point="/eliminarGrupo/"+codigo
    url_final= get_url + end_point
    return requests.delete(url_final)

def obtener_lista_grupos_con_limite(get_url,CODMATERIA):
    endpoint = "obtenerGrupoLimite/"+CODMATERIA+"/Modulo 4"
    lista_url = get_url + endpoint
    response = requests.get(lista_url)
    lista_grupos = response.json()
    return lista_grupos

def crear_grupo_limite(get_url,CODMATERIA,limite):
    end_point = "agregarGrupo"
    nombre_grupo=obtener_nombre_grupo()
    codigo=generar_cod(nombre_grupo)
    payload=generar_payload_limite(CODMATERIA,nombre_grupo,codigo,limite)
    url_final = get_url + end_point
    requests.post(url_final, json=payload)
    return codigo

#def crear_grupo(get_url):
#    lista_cursos = obtener_cursos(get_url)
#    CODCURSO = random.choice(lista_cursos)["CODCURSO"]
#    logger.debug(f"Curso seleccionado: {CODCURSO}")
#    crear_grupo(get_url,CODCURSO)
#    return CODCURSO

def obtener_grupo(get_url,cod_materia,cod_grupo):
    lista=obtener_lista_grupos(get_url,cod_materia)
    grupo = next(g for g in lista if g["CODGRUPO"] == cod_grupo)
    logger.debug(f"Grupo creado y obtenido: {grupo}")
    return grupo