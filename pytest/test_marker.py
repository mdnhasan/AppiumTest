import pytest


@pytest.mark.functional
def test_login():
    print("Login")


@pytest.mark.regression
def test_reg():
    print("Registration")


@pytest.mark.functional
def test_compose_mail():
    print('Sent Mail')

@pytest.mark.skip
def test_skip():
    print("Skipping Test")