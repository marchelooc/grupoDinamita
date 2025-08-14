import pytest
from src.api_infinity_chess.generar_info_curso import realizar_eliminacion
from src.utils.generador_codigo import generar_cod_letras
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue MABUG001: No responde correctamente cuando se elimina un grupo con id invalido", run=True)
def test_verificar_que_se_elimine_un_grupo_con_id_solo_letras(get_url):
    logger.info("Iniciando test MAM027.")
    #crear grupo
    codigo=generar_cod_letras()
    #eliminar grupo
    response = realizar_eliminacion(get_url,codigo)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code==404
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_eliminar_grupo.json"))
    logger.info("Test completado.") 