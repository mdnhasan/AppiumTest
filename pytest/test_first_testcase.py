import pytest

def setup_module(module):
    """Module level setup for each test case"""
    print("Create Connection")

def teardown_module(module):
    """Module level setup for each test case"""
    print("Disconnected")

def setup_function(function):
    """Function level setup for each test case"""
    print("Lunch Browser")

def teardown_function(function):
    """Function level setup for each test case"""
    print("Quit Browser")

def test_doLogin():
    print("Execute First TestCase")

def test_user_Reg():
    print("Execute User Reg")