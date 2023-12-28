import pytest

def test_validate():
    expected_title = 'google'
    actual_title = 'gmail'
    title = 'gmails'

    assert expected_title == actual_title, 'Titles are not matching'
    assert 'gmails' in title, 'gmail is not their in title'
    assert False