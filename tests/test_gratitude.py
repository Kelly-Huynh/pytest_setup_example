from lib.gratitude import Gratitudes


"""
Initially, the output is an incomplete sentence
"""
def test_initially_output_is_an_empty_string():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "

"""
When we add multiple strings
The output is those strings concatenated
"""

def test_adding_multiple_strings_outputs_concatenated():
    gratitude = Gratitudes()
    gratitude.add("my health")
    gratitude.add("my strengths")
    gratitude.add("my loved ones")
    assert gratitude.format() == "Be grateful for: my health, my strengths, my loved ones"