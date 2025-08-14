from src.api_infinity_chess.obtener_trabajadores import obtener_trabajadores
from src.utils.generador_codigo import generar_cod_inscripcion, generar_nombre, obtener_precio,generar_fecha_menor
import random
from datetime import datetime

generos_dic = {
     "Simon": "Hombre",
     "Ander": "Hombre",
     "Andrea": "Mujer",
     "Benjamin": "Hombre",
     "Carmen": "Mujer",
     "Isabel": "Mujer",
     "Raquel": "Mujer",
     "Dylan": "Hombre",
     "Dominic": "Hombre",
}

def determinar_genero(nombre):
     if nombre in generos_dic:
          return generos_dic[nombre]
     if nombre.endswith("a"):
          return "Mujer"
     elif nombre.endswith("o"):
          return "Hombre"
     elif nombre.endswith("e"):
          return "Hombre" if nombre in ["José", "Pepe"] else "Mujer"
     else:
          return "Hombre" 
     
def separar_nombre_completo(nombre_completo,  i):
     partes = nombre_completo.strip().split()
     if len(partes) < 2:
          raise ValueError("Se requiere al menos un nombre y un apellido.")
     return partes[i]

def crear_payload_estudiante():
     nombre_completo = generar_nombre()
     cod_estudiante = generar_cod_inscripcion(nombre_completo)
     nombre = separar_nombre_completo(nombre_completo,0)
     apellido = separar_nombre_completo(nombre_completo,1)
     fecha_nacimiento = generar_fecha_menor()
     genero = determinar_genero(nombre)
     return {
          "CODESTUDIANTE": cod_estudiante,
          "NOMBREESTUDIANTE": nombre,
          "APELLIDOESTUDIANTE": apellido,
          "FECHANACIMIENTOESTUDIANTE": fecha_nacimiento,
          "GENEROESTUDIANTE": genero,
          "DIRECCION": "Km 5 1/2 Cap. Uztariz",
          "PAIS": "Bolivia",
          "DEPARTAMENTO": "Cochabamba",
          "CIUDAD": "Cercado",
          "COLEGIO": "Fatima",
          "TURNO": "Mañana",
          "CURSO": "4º Primaria",
          "TIPOCOLEGIO": "Particular",
          "HABILITADO": "Habilitado",
          "SEDE": "Modulo 4",
          "HUELLA": "Virtual"
     }
     
def crear_payload_update_estudiante (estudiante):
     return {
          "NOMBREESTUDIANTE": estudiante["NOMBREESTUDIANTE"] + "E",
          "APELLIDOESTUDIANTE": estudiante["APELLIDOESTUDIANTE"] + "E",
          "DIRECCION": "Km 10 Cap. Uztariz",
          "PAIS": "Peru",
          "DEPARTAMENTO": "Cuzco",
          "CIUDAD": "San Sebastian",
          "COLEGIO": "Fatima",
          "TURNO": "Tarde",
          "CURSO": "4º Primaria",
          "TIPOCOLEGIO": "Fiscal",
     }