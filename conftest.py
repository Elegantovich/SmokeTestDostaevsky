import pytest


@pytest.fixture(scope="function")
def set_up():
    print("Start testing")
    yield
    print("Finish testing")
