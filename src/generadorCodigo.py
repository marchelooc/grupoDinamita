from datetime import datetime, timedelta
import random
import string

def generarCodigo():
    numero = str(random.randint(100000, 999999))
    letras = ''.join(random.choices(string.ascii_uppercase, k=6))
    return numero + letras


def generarNomMateria():
    materia = random.choice(materias)
    return f"{materia}"
    
 # Listas base de materias
materias = [
    "ruso", "español", "quechua", "italiano", "japones", "chino",
    "mandarin", "aitiano", "franses", "aleman", "arabe", "aymara"
]


def obtenerNombreGrupo():
    grupos = ["Grupo1", "Grupo2", "Grupo3", "Grupo4", "Grupo5","Grupo6", "Grupo7", "Grupo8", "Grupo9", "Grupo10",
            "Grupo11", "Grupo12", "Grupo13", "Grupo14", "Grupo15","Grupo16", "Grupo17", "Grupo18", "Grupo19", "Grupo20"]
    return random.choice(grupos)
    

def obtenerDias():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes","Sabado"]
    
    # Seleccionar aleatoriamente entre 2 y 5 días
    cantidad = random.randint(1, 6)
    
    # Seleccionar los días aleatorios
    ListaDeDias = random.sample(dias, cantidad)
    
    return ListaDeDias
    

def obtenerHoras():
    Horas = ["06:00","07:00", "08:00", "09:00", "10:00", "11:00","12:00","13:00","14:00","15:00","16:00",
            "17:00","18:00","19:00","20:00","21:00"]
    return random.choice(Horas)

def obtenerLimite():
    Limite=random.randint(1,30)
    return Limite

def obtenerPrecio():
    precio=random.randint(1,100)
    return precio


def generarCod (cod):
    año = datetime.now().year
    return f"{año}{cod}"