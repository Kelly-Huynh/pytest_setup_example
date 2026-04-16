from lib.report_length import *
import pytest

"""
If the string is empty
Returns 0
"""

def test_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."

"""
If the string has special characters and spaces
Returns length including special characters and spaces
"""

def test_string_with_special_characters():
    result = report_length("Hi!")
    assert result == "This string was 3 characters long."

"""
If the string is only special characters
Returns length of the string
"""    

def test_report_length_only_special_characters():
    result = report_length("!@*£$")
    assert result == "This string was 5 characters long."

# """
# If the argument passed is a boolean
# Returns an error gracefully
# """

# def test_report_length_boolean_values():
#     result = report_length(True)
#     assert result == "That wasn't a string you gave me."

# """
# If the argument passed is an int
# Returns an error gracefully
# """

# def test_report_length_int_values():
#     result = report_length(1)
#     assert result == "That wasn't a string you gave me."

"""
If the argument passed is a datatype that is not a string
Returns an error gracefully
"""
test_data = [2, 1.5, True, False]
@pytest.mark.parametrize("value", test_data)
def test_report_length_multiple_datatypes(value):
    result = report_length(value)
    assert result == "That wasn't a string you gave me."
