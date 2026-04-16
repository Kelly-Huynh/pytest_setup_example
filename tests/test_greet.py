from lib.greet import *

# def test_greet():
#     name = "Mike"
#     result = f"Hello {name}"
#     assert result == "Hello Mike"


def test_greet_person_of_given_name():
    result = greet("Kay")
    assert result == "Hello, Kay!"