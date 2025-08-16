import pytest
from src.api_infinity_chess.generar_info_curso import codigo_curso, realizar_eliminacion, crear_grupo , obtener_lista_grupos
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_verificar_que_se_elimine_un_grupo_con_id_valido(get_url):
    logger.info("Iniciando test MAM019.")
    CODMATERIA = codigo_curso(get_url)
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    #crear grupo
    codigo=crear_grupo(get_url,CODMATERIA)
    #eliminar grupo
    response = realizar_eliminacion(get_url,codigo)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==200
    lista_grupos = obtener_lista_grupos(get_url,CODMATERIA)
    codigos_actuales = [g["CODGRUPO"] for g in lista_grupos]
    # Validar que ya no existe
    assert codigo not in codigos_actuales, f"ERROR: El grupo '{codigo}' todavía existe."
    logger.info(f"El grupo '{codigo}' fue eliminado correctamente y ya no existe en la lista.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_eliminar_grupo.json"))
    logger.info("Test completado.") 