import pytest


def test_validate_titles():
    expected_result = "Google.com"
    actual_result = "gmail.com"
    title='This is gmail website'

    # if actual_result == expected_result:
    #     print("Test Case Pass")
    # else:
    #     print("Test Case Fail")
    """assert method"""
    print("Beginning")
    assert actual_result == expected_result, "Titles are not matched"

    assert 'gmails' in title, 'Title isnt matching'
    assert False, "Forcefully Fail"

    print("ENding")


"""Soft Assert COmmand in Terminal"""
"""pytest test_validate_title.py -s -v --soft-asserts"""
