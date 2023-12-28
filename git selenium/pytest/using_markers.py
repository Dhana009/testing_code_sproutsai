import pytest


@pytest.mark.functional
def test_login():
    print('testing login')


@pytest.mark.regression
def test_second_login():
    print('testing second login')


@pytest.mark.regression
def test_third_login():
    print('testing test_third_login')


@pytest.mark.skip
def test_fourth_login():
    print('testing skip')