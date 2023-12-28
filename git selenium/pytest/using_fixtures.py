import pytest

@pytest.fixture(scope='module')
def setup():
    print('first step')


    yield
    print('last step')


@pytest.fixture(scope='function')
def function_level():
    print('at function start level')

    yield
    print('at function last level')


@pytest.mark.usefixtures('setup','function_level')
def test_login():
    print('testing login')


@pytest.mark.usefixtures('setup')
def test_second_login():
    print('testing second login')