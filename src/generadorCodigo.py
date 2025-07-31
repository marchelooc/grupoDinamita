from datetime import datetime, timedelta
import random
import string

def generarCodigo():
    numero = str(random.randint(100000, 999999))
    letras = ''.join(random.choices(string.ascii_uppercase, k=6))
    return numero + letras

def generarCodigoTrab(nombre: str) -> str:
    fechaHoy = datetime.now().strftime("%Y%m%d")  
    return f"{fechaHoy}{nombre[:5].upper()}"

def generarNombre():
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    return f"{nombre} {apellido}"
    
# Listas base de nombres y apellidos
nombres = [
    "Carlos", "María", "Ana", "Luis", "José", "Lucía",
    "Pedro", "Camila", "Andrés", "Valeria", "Diego", "Fernanda"
]

apellidos = [
    "Pérez", "Gómez", "Rodríguez", "Martínez", "López",
    "Sánchez", "Gutiérrez", "Ramírez", "Torres", "Vargas"
]    


from datetime import datetime, timedelta

def generarFechaNac(edad_min=18, edad_max=75):
    hoy = datetime.today()
    dias_min = edad_min * 365
    dias_max = edad_max * 365

    # Genera un número aleatorio de días entre esos rangos
    dias_random = random.randint(dias_min, dias_max)

    # Resta esos días a la fecha de hoy
    fecha_nacimiento = hoy - timedelta(days=dias_random)
    return fecha_nacimiento.strftime("%Y-%m-%d")  # formato YYYY-MM-DD


def generarContraseña(longitud=10, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_lowercase  # letras minúsculas

    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña