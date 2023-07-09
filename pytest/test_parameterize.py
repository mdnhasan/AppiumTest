import pytest


def getData():
    return [

        ('nasim@gmail.com', '123'),
        ('nirob@yahoo.com', '123'),
        ('sam@hotmail.com', '123')

    ]


@pytest.mark.parametrize("username,password", getData())
def test_login(username, password):
    print(username,  "---", password)
