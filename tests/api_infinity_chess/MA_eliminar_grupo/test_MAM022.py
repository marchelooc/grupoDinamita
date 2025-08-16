import pytest
from src.api_infinity_chess.generar_info_curso import codigo_curso, realizar_eliminacion, crear_grupo , obtener_lista_grupos, eliminar_grupo
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
@pytest.mark.xfail(reason="Knwon issue MABUG001: No responde correctamente cuando se elimina un grupo con id que ya no existe", run=True)
def test_verificar_que_se_elimine_un_grupo_por_segunda_vez(get_url):
    logger.info("Iniciando test MAM019.")
    CODMATERIA = codigo_curso(get_url)
    logger.debug(f"Codigo materia seleccionado: {CODMATERIA}.")
    codigo=crear_grupo(get_url,CODMATERIA) #crear grupo
    eliminar_grupo(get_url,codigo)# eliminacion primera vez
    response = realizar_eliminacion(get_url,codigo)#eliminar segunda vez
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==404
    try:
        data = response.json()
    except ValueError:
        data = None 
    if data:
        logger.info("Validando schema del response.")
        assert_validar_response_schema(response,cargar_schema("schema_eliminar_grupo.json"))
    logger.info("Test completado.") 