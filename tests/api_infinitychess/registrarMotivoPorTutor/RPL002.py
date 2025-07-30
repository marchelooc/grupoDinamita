import requests
import pytest
import jsonschema
import random
from src.obtenerTutores import obtenerTutoresActivos

@pytest.mark.smoke
def test_RPL002_registroMotivoExitoso (getUrl):
    listaTutores = obtenerTutoresActivos(getUrl)
    codtutor = random.choice(listaTutores)["CODTUTOR"]
    endpoint = "agregarMotivo" 
    lista_url = getUrl + endpoint

    payload = { "CODTUTOR": codtutor, "MOTIVO": "prueba", "FECHAMOTIVO": "2025-7-30", "ESTADO": "Activo" }
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'XSRF-TOKEN=eyJpdiI6Ik16a01INGxERGpHcVAwTVZTcG8vWXc9PSIsInZhbHVlIjoiRHpPSGpTalF3M0dOOTZzL293d2IxR01Dbk9mVC9ZM2pHUXJqenBoejdTNmNtYURMSi9MQVo0dEpaTUx2bldwUGZyT0RJNThUN0xnYXRBd0xyWGl0TmZYNXM1U0RKL0lmbERWVGl0ckJzL2dvLzBISnVtVXRYR1ZjN3UwVEF6ZGYiLCJtYWMiOiI3OTYzYzNiMDk3Y2RkMDliZmJiZGIzODBhOWVhN2I0Mzg5YjIwZjE4OTBlOTcxYWUxMmQwNGFiODE2MTRiN2FhIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6ImxCRjZ3VDAxRmN0bklSYllaVkdRd0E9PSIsInZhbHVlIjoialJsT1Y0cjc2OU90RHVyVmtGSmkwcVdCVUVZZUVwRncyR2J5LzlEalZPTHZCSEt3RzkzajczUjVjZ2oxS3VRM3hXS0ZPRU1IREdESk5VN1pYeEJSSHVzUTZJL25Pa0J5U0NodG9Sc1UrRTh3Vmdwb3dJdzNuUTJGaGR2MDJhNTAiLCJtYWMiOiIzNjc4OGIxMzZmNDgyYWI0NzI5OWQ5ODU3Yjk1MjQyMTI0NWM1OTBhMDE1MGY2YjVjMGUwMjIyMzgxNjcxNjFhIiwidGFnIjoiIn0%3D'
    }

    response = requests.post(lista_url, headers=headers, json=payload)
    assert response.status_code == 201
    schema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": [
        "CODTUTOR",
        "ESTADO",
        "FECHAMOTIVO",
        "MOTIVO"
    ],
    "properties": {
        "CODTUTOR": {
        "type": "string"
        },
        "MOTIVO": {
        "type": "string"
        },
        "FECHAMOTIVO": {
        "type": "string"
        },
        "ESTADO": {
        "type": "string"
        }
    }
    }
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema no coincide: {err}")
