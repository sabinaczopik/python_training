import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixtura = Application()
    request.addfinalizer(fixtura.destroy)
    return fixtura