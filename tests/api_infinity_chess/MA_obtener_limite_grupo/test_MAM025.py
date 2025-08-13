import pytest
from src.api_infinity_chess.generar_info_curso import codigo_curso, crear_grupo_limite, obtener_lista_grupos_con_limite
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_verificar_comportamiento_del_limite_lleno(get_url):
    logger.info("Iniciando test MAM023.")
    CODMATERIA = codigo_curso(get_url)
    logger.debug(f"Curso seleccionado: {CODMATERIA}")
    limite_diponible=4 # 1 a 4 cupos restante = LLENO
    codigo=crear_grupo_limite(get_url,CODMATERIA,limite_diponible)
    lista_grupos = obtener_lista_grupos_con_limite(get_url,CODMATERIA)
    limite_real = next(g["LIMITE"] for g in lista_grupos if g["CODGRUPO"] == codigo)
    limite_esperado = "LLENO" 
    assert limite_real == limite_esperado
    logger.info(f"El límite del grupo '{codigo}' es correcto: {limite_real}")
    