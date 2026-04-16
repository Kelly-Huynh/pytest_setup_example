import pytest
from lib.password_checker import PasswordChecker

"""
To test if a password is 9 characters
Returns True
"""
def test_password_checker_for_nine_chars():
    password = PasswordChecker()
    password.check("123456789")
    assert True

"""
To test if a password is 7 characters
Returns error
"""
def test_password_checker_for_seven_chars():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."