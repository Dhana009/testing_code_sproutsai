import pytest

def get_data():
    return[
        ('apple','pandu'),
        ('banana','pandu')
    ]



@pytest.mark.parametrize('username,password',get_data())
def test_do_login(username, password,chrome_browser):
    print(username, '---', password)
    driver = chrome_browser
    driver.get('https://google.com')

