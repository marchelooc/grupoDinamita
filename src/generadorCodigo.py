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
