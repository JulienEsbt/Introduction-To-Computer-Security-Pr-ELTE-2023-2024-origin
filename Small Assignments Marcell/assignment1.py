def test_function(input): 
    chars = [chr(i) for i in input]
    string_upper = ''.join(chars)
    string_lower = string_upper.lower()
    return string_lower[2:10] * 2
