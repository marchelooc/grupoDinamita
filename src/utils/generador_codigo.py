from datetime import datetime, timedelta
import random
import string

def generar_codigo():
    numero = str(random.randint(100000, 999999))
    letras = ''.join(random.choices(string.ascii_uppercase, k=6))
    return numero + letras



def obtener_nombre_grupo():
    grupos = ["Grupo1", "Grupo2", "Grupo3", "Grupo4", "Grupo5","Grupo6", "Grupo7", "Grupo8", "Grupo9", "Grupo10",
            "Grupo11", "Grupo12", "Grupo13", "Grupo14", "Grupo15","Grupo16", "Grupo17", "Grupo18", "Grupo19", "Grupo20"]
    return random.choice(grupos)
    

def obtener_nombre_grupo_2_caracteres():
    grupos = ["AA", "Ba", "CC", "De", "EE","FF", "GG", "HH", "II", "MM",
            "NN", "12", "34", "GH", "ZZ","LL", "RR", "PP", "QQ", "JJ", "KK", "KL"]
    return random.choice(grupos)

def obtener_nombre_grupo_3_caracteres():
    grupos = ["AAa", "Bat", "CCf", "Deh", "EEc","FFh", "GGi", "HoH", "IaI", "MeM",
            "NN", "1f2", "3r4", "GHi", "ZcZ","LmL", "RvR", "PrP", "QuQ", "JoJ", "KaK", "KiL"]
    return random.choice(grupos)

def obtener_dias():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes","Sabado"]
    
    # Seleccionar aleatoriamente entre 2 y 5 días
    cantidad = random.randint(1, 6)
    
    # Seleccionar los días aleatorios
    lista_de_dias = random.sample(dias, cantidad)
    
    return lista_de_dias
    

def obtener_horas():
    horas = ["06:00","07:00", "08:00", "09:00", "10:00", "11:00","12:00","13:00","14:00","15:00","16:00",
            "17:00","18:00","19:00","20:00","21:00"]
    return random.choice(horas)

def obtener_limite():
    limite=random.randint(1,30)
    return limite

def obtener_precio():
    precio=random.randint(1,100)
    return precio


def generar_cod (cod):
    año = datetime.now().year
    return f"{año}{cod}"

def generar_cod_inscripcion(nombre_completo):
    partes = nombre_completo.strip().split()
    
    # Asegurar que haya al menos 2 partes (nombre y apellido)
    if len(partes) < 2:
        raise ValueError("Se requiere al menos un nombre y un apellido.")
    
    nombre = partes[0]
    apellido = partes[1]

    sub_nombre = nombre[:3]
    sub_apellido = apellido[:3]

    ahora = datetime.now()
    año = ahora.year
    mes = ahora.month
    dia = ahora.day

    codigo = f"{año}{mes:02}{dia:02}{sub_nombre}{sub_apellido}"
    return codigo.upper()

def generarCodigoTrab(nombre: str) -> str:
    fechaHoy = datetime.now().strftime("%Y%m%d")  
    return f"{fechaHoy}{nombre[:5].upper()}"

def generar_nombre():
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

def generar_nom_materia():
    materias = ["Ingles", "Ruso", "Esñaol", "Quechua", "Mandarín","Polaco", "Árabe", "Birmano",
            "Chino", "Yoruba", "Japones", "Indonesio", "Portugues","Frances", "Italiano"]
    return random.choice(materias)


