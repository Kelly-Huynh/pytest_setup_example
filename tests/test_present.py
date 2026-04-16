import pytest
from lib.present import Present

"""
Initially reports none content has been wrapped.
"""

def test_class_init():
    present = Present()
    assert present.contents == None

"""
Initially reports one content has been wrapped.
"""

def test_wrap_stored_contents():
    present = Present()
    present.wrap("perfume set")
    assert present.contents == "perfume set"

"""
When we wrap an item
We get it back from unwrapping
(happy case)
"""

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33


"""
If we unwrap before wrapping
We get an error message
(error case)
"""
def test_unwrap_without_wrapping():
    present = Present()
    # assert present.unwrap() == "ewsazvdx" <-- can't do this w/e the error msg is '
    # as it's not the right context to catch and assert on that error message, instead:
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."


"""
If we try to wrap an already-wrapped present
We get an error message
"""
def test_wrapping_already_wrapped_throws_error():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    message = str(e.value)
    assert message == "A contents has already been wrapped."


"""
If we try to wrap an already-wrapped present
The first-wrapped value is unchanged
"""
def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    assert present.unwrap() == 44

"""
Testing wrap method
Returns sad path
"""
def test_wrap_raises_exception():
    present = Present()
    present.wrap("perfume set")
    with pytest.raises(Exception) as e:
        present.wrap("gift set")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
    

"""
Testing unwrap method
Returns happy path
"""

def test_unwrap_returns_stored_contents():
    present = Present()
    present.wrap("perfume set")
    result = present.unwrap()
    assert result == "perfume set"

"""
Testing unwrap method
Returns sad path
"""

def test_unwrap_raises_exception():
    present = Present()
    with pytest.raises(Exception) as e: # <-- New code
        present.unwrap()
    error_message = str(e.value) # <-- New code
    assert error_message == "No contents have been wrapped."

"""
Testing wrap and unwrap method - combination
Returns happy path
"""

def test_present_initially_reports_one_wrapped():
    present = Present()
    present.wrap("perfume set")
    result = present.unwrap() 
    assert result == "perfume set"
    # assert result == "A contents has been wrapped."



"""
To report no contents have been wrapped
"""
# def test_present_initially_reports_none_wrapped():
#     present = Present()
#     assert present.unwrap() == "No contents have been wrapped."


def test_present():
    present = Present()
    with pytest.raises(Exception) as e: # <-- New code
        present.unwrap()
    error_message = str(e.value) # <-- New code
    assert error_message == "No contents have been wrapped."