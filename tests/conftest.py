import pytest
from config import get_base_url

# Agrega esto arriba
import os
from dotenv import load_dotenv
import sys

# Cargar variables desde el archivo .env
load_dotenv()

# Añadir PYTHONPATH del .env a sys.path si no está
py_path = os.getenv("PYTHONPATH")
if py_path and py_path not in sys.path:
    sys.path.insert(0, py_path)

# Tu fixture sigue igual
@pytest.fixture
def getUrl():
    return get_base_url()
