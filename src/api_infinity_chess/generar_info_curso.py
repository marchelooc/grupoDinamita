import random
import requests
from src.api_infinity_chess.obtener_curso import obtener_cursos
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.payload.generar_payload_grupo import generar_payload_duplicado,generar_payload_eliminar, generar_payload_limite_disp
from src.utils.generador_codigo import obtener_nombre_grupo, generar_cod
from src.utils.response_500 import response_500
from src.utils.logger_config import logger

def codigo_curso(get_url):
    lista_cursos = obtener_cursos(get_url)
    CODCURSO = random.choice(lista_cursos)["CODCURSO"]
    return CODCURSO

def realizar_peticion(get_url,payload):
    end_point = "agregarGrupo"
    url_final = get_url + end_point
    logger.info(f"Enviando POST a {url_final}.")
    response=requests.post(url_final, json=payload)
    response_500(response)
    return response

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
    logger.info(f"Código de respuesta: {response.status_code}.")
    lista_grupos = response.json()
    logger.debug(f"La lista es: {lista_grupos}")
    return lista_grupos

def crear_grupo_limite(get_url,CODMATERIA,limite):
    end_point = "agregarGrupo"
    nombre_grupo=obtener_nombre_grupo()
    codigo=generar_cod(nombre_grupo)
    payload=generar_payload_limite_disp(CODMATERIA,nombre_grupo,codigo,limite)
    url_final = get_url + end_point
    requests.post(url_final, json=payload)
    return codigo

def validar_respuesta(response):
    try:
        data = response.json()
    except ValueError:
        data = None 
    if data:
        logger.info("Validando schema del response.")
        assert_validar_response_schema(response,cargar_schema("schema_eliminar_grupo.json"))

        
def verificar_limite_lleno(lista_grupos,codigo):
    limite_real = next(g["LIMITE"] for g in lista_grupos if g["CODGRUPO"] == codigo)
    limite_esperado = "LLENO" 
    assert limite_real == limite_esperado
    logger.info(f"El límite del grupo '{codigo}' es correcto: {limite_real}")

def verificar_limite_casi(lista_grupos,codigo):
    limite_real = next(g["LIMITE"] for g in lista_grupos if g["CODGRUPO"] == codigo)
    limite_esperado = "CASI" 
    assert limite_real == limite_esperado
    logger.info(f"El límite del grupo '{codigo}' es correcto: {limite_real}")

def verificar_limite_hay(lista_grupos,codigo):
    limite_real = next(g["LIMITE"] for g in lista_grupos if g["CODGRUPO"] == codigo)
    limite_esperado = "HAY" 
    assert limite_real == limite_esperado
    logger.info(f"El límite del grupo '{codigo}' es correcto: {limite_real}")
        

def obtener_grupo(get_url,cod_materia,cod_grupo):
    lista=obtener_lista_grupos(get_url,cod_materia)
    grupo = next(g for g in lista if g["CODGRUPO"] == cod_grupo)
    logger.debug(f"Grupo creado y obtenido: {grupo}")
    return grupo

def verificar_eliminacion(lista_grupos,codigo):
    codigos_actuales = [g["CODGRUPO"] for g in lista_grupos]
    assert codigo not in codigos_actuales, f"ERROR: El grupo '{codigo}' todavía existe."
    logger.info(f"El grupo con codigo:'{codigo}' fue eliminado correctamente y ya no existe en la lista.")