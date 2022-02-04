import pytest


def pytest_addoption(parser):
    parser.addoption("--rounding_index", action="store", default="1", help="Type the rounding index")


@pytest.fixture
def rounding_index(request):
    request.cls.rounding_index = request.config.getoption("–-rounding_index")
