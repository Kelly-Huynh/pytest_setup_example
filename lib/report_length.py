#original challenge

def report_length(str):
    length = len(str)
    return f"This string was {length} characters long."

#updated challenge to test out with parametrize

def report_length(string):
    if (isinstance(string, str)):
        length = len(string)
        return f"This string was {length} characters long."
    
    return "That wasn't a string you gave me."
    