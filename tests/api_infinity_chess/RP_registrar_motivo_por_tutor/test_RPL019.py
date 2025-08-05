import requests
import pytest
import jsonschema
import random
from src.api_infinity_chess.obtener_tutores import obtener_tutores_activos
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from datetime import date, timedelta
from src.utils.logger_config import logger 

@pytest.mark.funtional
@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue RPBUG005: Crea motivos con fecha de motivo antigua",run=True)
def test_RPL019_registro_motivo_con_FECHAMOTIVO_antigua (get_url):
    logger.info("Iniciando Test Case RPL019")
    logger.info(get_url)
    lista_tutores = obtener_tutores_activos(get_url)
    cod_tutor = random.choice(lista_tutores)["CODTUTOR"]
    endpoint = "agregarMotivo" 
    lista_url = get_url + endpoint
    logger.debug(lista_url)
    fecha_antigua = (date.today() - timedelta(days=1000)).strftime("%d/%m/%Y") 
    payload = { "CODTUTOR": cod_tutor, "MOTIVO": "pruebe fecha -1000", "FECHAMOTIVO": fecha_antigua, "ESTADO": "Activo" }
    logger.debug(payload)
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'XSRF-TOKEN=eyJpdiI6Ik16a01INGxERGpHcVAwTVZTcG8vWXc9PSIsInZhbHVlIjoiRHpPSGpTalF3M0dOOTZzL293d2IxR01Dbk9mVC9ZM2pHUXJqenBoejdTNmNtYURMSi9MQVo0dEpaTUx2bldwUGZyT0RJNThUN0xnYXRBd0xyWGl0TmZYNXM1U0RKL0lmbERWVGl0ckJzL2dvLzBISnVtVXRYR1ZjN3UwVEF6ZGYiLCJtYWMiOiI3OTYzYzNiMDk3Y2RkMDliZmJiZGIzODBhOWVhN2I0Mzg5YjIwZjE4OTBlOTcxYWUxMmQwNGFiODE2MTRiN2FhIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6ImxCRjZ3VDAxRmN0bklSYllaVkdRd0E9PSIsInZhbHVlIjoialJsT1Y0cjc2OU90RHVyVmtGSmkwcVdCVUVZZUVwRncyR2J5LzlEalZPTHZCSEt3RzkzajczUjVjZ2oxS3VRM3hXS0ZPRU1IREdESk5VN1pYeEJSSHVzUTZJL25Pa0J5U0NodG9Sc1UrRTh3Vmdwb3dJdzNuUTJGaGR2MDJhNTAiLCJtYWMiOiIzNjc4OGIxMzZmNDgyYWI0NzI5OWQ5ODU3Yjk1MjQyMTI0NWM1OTBhMDE1MGY2YjVjMGUwMjIyMzgxNjcxNjFhIiwidGFnIjoiIn0%3D'
    }
    logger.info("validando Schema de payload")
    assert_validar_schema_input (payload, cargar_schema("schema_motivo.json"))
    response = requests.post(lista_url, headers=headers, json=payload)
    assert response.status_code == 400
    logger.info(response.status_code)
    logger.info("Validando response")
    assert_validar_response_schema (response, cargar_schema("schema_motivo.json"))