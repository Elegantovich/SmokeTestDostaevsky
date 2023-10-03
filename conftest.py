import pytest


@pytest.fixture(scope="module")
def set_up():
    print("Start testing")
    yield
    print("Finish testing")