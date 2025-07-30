
import pytest
from config import get_base_url

@pytest.fixture
def getUrl():
    return get_base_url()
