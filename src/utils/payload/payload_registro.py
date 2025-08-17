
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajadores
from src.api_infinity_chess.registro import obtener_estudiante_aleatorio_completo
from src.utils.generador_codigo import generar_cod_inscripcion, generar_codigo, obtener_precio
import random
from datetime import datetime, timedelta

payload_vacio = {
     "CODINSCRIPCION": "",
     "CODTRABAJADOR": "",
     "FECHAINSCRIPCION": "",
     "COSTOINSCRIPCION": 0,
     "CODSEDE": "",
     "HABILITADO": "",
     "CODESTUDIANTE": ""
}
def crear_payload_valido(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_estudiante = estudiante["CODESTUDIANTE"]
     cod_inscripcion = generar_cod_inscripcion(f"{estudiante['NOMBREESTUDIANTE']} {estudiante['APELLIDOESTUDIANTE']}")
     lista_trabajadores = obtener_trabajadores(get_url)
     cod_trabajador = random.choice(lista_trabajadores)["CODTRABAJADOR"]
     fecha_hoy = datetime.now().strftime("%Y-%m-%d")
     return {
          "CODINSCRIPCION": cod_inscripcion,
          "CODTRABAJADOR": cod_trabajador,
          "FECHAINSCRIPCION": fecha_hoy,
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "Modulo 4",
          "HABILITADO": "Habilitado",
          "CODESTUDIANTE": cod_estudiante
     }
     
def crear_payload_estudiante_invalido(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_estudiante = generar_codigo()
     cod_inscripcion = generar_cod_inscripcion(f"{estudiante['NOMBREESTUDIANTE']} {estudiante['APELLIDOESTUDIANTE']}")
     lista_trabajadores = obtener_trabajadores(get_url)
     cod_trabajador = random.choice(lista_trabajadores)["CODTRABAJADOR"]
     fecha_hoy = datetime.now().strftime("%Y-%m-%d")
     return {
          "CODINSCRIPCION": cod_inscripcion,
          "CODTRABAJADOR": cod_trabajador,
          "FECHAINSCRIPCION": fecha_hoy,
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "Modulo 4",
          "HABILITADO": "Habilitado",
          "CODESTUDIANTE": cod_estudiante
     }
     
def crear_payload_sin_codigo_inscripcion(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_estudiante = estudiante["CODESTUDIANTE"]
     lista_trabajadores = obtener_trabajadores(get_url)
     cod_trabajador = random.choice(lista_trabajadores)["CODTRABAJADOR"]
     fecha_hoy = datetime.now().strftime("%Y-%m-%d")
     return {
          "CODINSCRIPCION": "",
          "CODTRABAJADOR": cod_trabajador,
          "FECHAINSCRIPCION": fecha_hoy,
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "Modulo 4",
          "HABILITADO": "Habilitado",
          "CODESTUDIANTE": cod_estudiante
     }

def crear_payload_sin_codigo_trabajador(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_estudiante = estudiante["CODESTUDIANTE"]
     cod_inscripcion = generar_cod_inscripcion(f"{estudiante['NOMBREESTUDIANTE']} {estudiante['APELLIDOESTUDIANTE']}")
     fecha_hoy = datetime.now().strftime("%Y-%m-%d")
     return {
          "CODINSCRIPCION": cod_inscripcion,
          "CODTRABAJADOR": "",
          "FECHAINSCRIPCION": fecha_hoy,
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "Modulo 4",
          "HABILITADO": "Habilitado",
          "CODESTUDIANTE": cod_estudiante
     }
     
def crear_payload_sin_codigo_sede(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_estudiante = estudiante["CODESTUDIANTE"]
     cod_inscripcion = generar_cod_inscripcion(f"{estudiante['NOMBREESTUDIANTE']} {estudiante['APELLIDOESTUDIANTE']}")
     lista_trabajadores = obtener_trabajadores(get_url)
     cod_trabajador = random.choice(lista_trabajadores)["CODTRABAJADOR"]
     fecha_hoy = datetime.now().strftime("%Y-%m-%d")
     return {
          "CODINSCRIPCION": cod_inscripcion,
          "CODTRABAJADOR": cod_trabajador,
          "FECHAINSCRIPCION": fecha_hoy,
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "",
          "HABILITADO": "Habilitado",
          "CODESTUDIANTE": cod_estudiante
     }

def crear_payload_sin_codigo_estudiante(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_inscripcion = generar_cod_inscripcion(f"{estudiante['NOMBREESTUDIANTE']} {estudiante['APELLIDOESTUDIANTE']}")
     lista_trabajadores = obtener_trabajadores(get_url)
     cod_trabajador = random.choice(lista_trabajadores)["CODTRABAJADOR"]
     fecha_hoy = datetime.now().strftime("%Y-%m-%d")
     return {
          "CODINSCRIPCION": cod_inscripcion,
          "CODTRABAJADOR": cod_trabajador,
          "FECHAINSCRIPCION": fecha_hoy,
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "Modulo 4",
          "HABILITADO": "Habilitado",
          "CODESTUDIANTE": ""
     }

def crear_payload_habilitado_invalido(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_estudiante = estudiante["CODESTUDIANTE"]
     cod_inscripcion = generar_cod_inscripcion(f"{estudiante['NOMBREESTUDIANTE']} {estudiante['APELLIDOESTUDIANTE']}")
     lista_trabajadores = obtener_trabajadores(get_url)
     cod_trabajador = random.choice(lista_trabajadores)["CODTRABAJADOR"]
     fecha_hoy = datetime.now().strftime("%Y-%m-%d")
     return {
          "CODINSCRIPCION": cod_inscripcion,
          "CODTRABAJADOR": cod_trabajador,
          "FECHAINSCRIPCION": fecha_hoy,
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "Modulo 4",
          "HABILITADO": "Pendiente",
          "CODESTUDIANTE": cod_estudiante
     }
def crear_payload_trabajador_invalido(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_estudiante = estudiante["CODESTUDIANTE"]
     cod_inscripcion = generar_cod_inscripcion(f"{estudiante['NOMBREESTUDIANTE']} {estudiante['APELLIDOESTUDIANTE']}")
     cod_trabajador = generar_codigo()
     fecha_hoy = datetime.now().strftime("%Y-%m-%d")
     return {
          "CODINSCRIPCION": cod_inscripcion,
          "CODTRABAJADOR": cod_trabajador,
          "FECHAINSCRIPCION": fecha_hoy,
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "Modulo 4",
          "HABILITADO": "Habilitado",
          "CODESTUDIANTE": cod_estudiante
     }

def crear_payload_fecha_invalida(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_estudiante = estudiante["CODESTUDIANTE"]
     cod_inscripcion = generar_cod_inscripcion(f"{estudiante['NOMBREESTUDIANTE']} {estudiante['APELLIDOESTUDIANTE']}")
     lista_trabajadores = obtener_trabajadores(get_url)
     cod_trabajador = random.choice(lista_trabajadores)["CODTRABAJADOR"]     
     fecha_hoy = datetime.now().strftime("%d-%m-%y")
     return {
          "CODINSCRIPCION": cod_inscripcion,
          "CODTRABAJADOR": cod_trabajador,
          "FECHAINSCRIPCION": fecha_hoy,
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "Modulo 4",
          "HABILITADO": "Habilitado",
          "CODESTUDIANTE": cod_estudiante
     }

def crear_payload_fecha_pasada(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_estudiante = estudiante["CODESTUDIANTE"]
     cod_inscripcion = generar_cod_inscripcion(f"{estudiante['NOMBREESTUDIANTE']} {estudiante['APELLIDOESTUDIANTE']}")
     lista_trabajadores = obtener_trabajadores(get_url)
     cod_trabajador = random.choice(lista_trabajadores)["CODTRABAJADOR"]     
     fecha_pasada = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
     return {
          "CODINSCRIPCION": cod_inscripcion,
          "CODTRABAJADOR": cod_trabajador,
          "FECHAINSCRIPCION": fecha_pasada, 
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "Modulo 4",
          "HABILITADO": "Habilitado",
          "CODESTUDIANTE": cod_estudiante
     }

def crear_payload_fecha_futura(get_url):
     estudiante = obtener_estudiante_aleatorio_completo(get_url)
     cod_estudiante = estudiante["CODESTUDIANTE"]
     cod_inscripcion = generar_cod_inscripcion(f"{estudiante['NOMBREESTUDIANTE']} {estudiante['APELLIDOESTUDIANTE']}")
     lista_trabajadores = obtener_trabajadores(get_url)
     cod_trabajador = random.choice(lista_trabajadores)["CODTRABAJADOR"]     
     fecha_futura = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
     return {
          "CODINSCRIPCION": cod_inscripcion,
          "CODTRABAJADOR": cod_trabajador,
          "FECHAINSCRIPCION": fecha_futura, 
          "COSTOINSCRIPCION": obtener_precio(),
          "CODSEDE": "Modulo 4",
          "HABILITADO": "Habilitado",
          "CODESTUDIANTE": cod_estudiante
     }