import jsonschema
import pytest
from src.utils.logger_config import logger 

def assert_validar_response_schema(response, schema):
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
        logger.debug("Response validado correctamente con el Schema.")
        return True
    except jsonschema.exceptions.ValidationError as err:
        logger.debug(f"El Response no coincide con el Schema: {err.message}")
        pytest.fail(f"El Response no coincide con el Schema: {err.message}")

def assert_validar_schema_input(data, schema):
    try:
        jsonschema.validate(instance=data, schema=schema)
        logger.debug("Payload validado correctamente con el Schema.")
        return True
    except jsonschema.exceptions.ValidationError as err:
        logger.debug(f"El Payload no coincide con el Schema: {err.message}")
        pytest.fail(f"El Payload no coincide con el Schema: {err.message}")
