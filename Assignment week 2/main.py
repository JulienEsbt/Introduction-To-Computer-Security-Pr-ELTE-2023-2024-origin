def test_function(int_list):
    char_list = [chr(num) for num in int_list]
    char_string = ''.join(char_list)
    char_string_lower = char_string.lower()
    result = char_string_lower[2:10] * 2
    return result