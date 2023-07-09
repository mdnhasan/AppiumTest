import pytest


@pytest.fixture(scope='module')
def module():
    print("Create Connection")

    yield
    print("Close COnnection")


@pytest.fixture(scope='function')
def function():
    print("Open Browser")

    yield
    print("Close Broswer")


"""Method to add module and function"""
# def test_doLogin(module,function):
#     print("Execute login")
#
# def test_user_Reg(module,function):
#     print("Execute reg")
#
# def test_user_text():
#     print("Third Log")

"""ANother method to add pytest fixture """


@pytest.mark.usefixtures('module', 'function')
def test_doLogin():
    print("Execute login")


@pytest.mark.usefixtures('module', 'function')
def test_user_Reg():
    print("Execute reg")


@pytest.mark.usefixtures('module', 'function')
def test_user_text():
    print("Third Log")
