def hex2string(hex_string):
    result = ""

    # Iterate through the input (with steps of 2 characters)
    for i in range(0, len(hex_string), 2):
        # Extract two characters from the input
        hex_pair = hex_string[i:i + 2]

        # Convert the hex pair to a character
        char_code = int(hex_pair, 16)
        result += chr(char_code)

    return result


# Tests :
# print('Function hex2string : ')
# print(hex2string('61'))          # Output: 'a'
# print(hex2string('776f726c64'))   # Output: 'world'
# print(hex2string('68656c6c6f'))   # Output: 'hello'
# print()

######################################################################
def string2hex(text):
    hex_string = ""

    # Iterate through each character in the input
    for char in text:
        # Convert the character to its ASCII code in hexadecimal form
        hex_code = hex(ord(char))[2:]

        # Ensure the hex code is two characters long ('01' instead of '1')
        if len(hex_code) == 1:
            hex_code = '0' + hex_code

        hex_string += hex_code

    return hex_string


# Tests :
# print('Function string2hex : ')
# print(string2hex('a'))           # Output: '61'
# print(string2hex('hello'))       # Output: '68656c6c6f'
# print(string2hex('world'))       # Output: '776f726c64'
# print(string2hex('foo'))         # Output: '666f6f'
# print()

######################################################################
def hex_xor(hex_str1, hex_str2):
    # Ensure that both input strings have the same length
    if len(hex_str1) != len(hex_str2):
        raise ValueError("Input strings must have the same length")

    result = ''

    # Perform bitwise XOR operation on each pair of corresponding characters
    for char1, char2 in zip(hex_str1, hex_str2):
        # Convert hexadecimal characters to integers
        int1 = int(char1, 16)
        int2 = int(char2, 16)

        # Perform the XOR operation and convert the result back to hexadecimal
        xor_result = int1 ^ int2
        result += format(xor_result, 'x')

    return result


# Tests :
# print('Function hex_xor : ')
# print(hex_xor('0aabbf11', '12345678'))  # Output: '189fe969'
# print(hex_xor('12cc', '12cc'))          # Output: '0000'
# print(hex_xor('1234', '2345'))          # Output: '3171'
# print(hex_xor('111', '248'))            # Output: '359'
# print(hex_xor('8888888', '1234567'))    # Output: '9abcdef'

######################################################################
def encrypt_single_byte_xor(input_hex, key_hex):
    # Adapt the key so that the input and the key have the same length
    key_hex = key_hex * (len(input_hex) // len(key_hex) + 1)

    result = ''

    # Perform bitwise XOR operation on each pair of corresponding characters
    for char_input, char_key in zip(input_hex, key_hex):
        # Convert hexadecimal characters to integers
        int_input = int(char_input, 16)
        int_key = int(char_key, 16)

        # Perform the XOR operation and convert the result back to hexadecimal
        xor_result = int_input ^ int_key
        result += format(xor_result, 'x')

    # --> Use hex_xor function instead of this function

    return result

# Tests :
# print('Function encrypt_single_byte_xor : ')
# print(encrypt_single_byte_xor('aaabbccc', '00'))
# Output: 'aaabbccc'
# print(encrypt_single_byte_xor(string2hex('hello'), 'aa'))
# Output: 'c2cfc6c6c5'
# print(hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('hello'),'aa'),'aa')))
# Output: 'hello'
# print(hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('Encrypt and decrypt are the same'),'aa'),'aa')))
# Output: 'Encrypt and decrypt are the same'

######################################################################
def decrypt_single_byte_xor(encrypted_hex):
    valid_characters = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVXYZ"

    best_score = 0
    best_decrypted_text = ""

    for key in range(256):  # Try all possible one-byte keys
        key_hex = format(key, '02x') * (len(encrypted_hex) // 2)
        decrypted_hex = encrypt_single_byte_xor(encrypted_hex, key_hex)
        decrypted_text = hex2string(decrypted_hex)

        # Calculate the score based on the number of valid characters
        score = sum(1 for char in decrypted_text if char in valid_characters)

        if score > best_score:
            best_score = score
            best_decrypted_text = decrypted_text

    return best_decrypted_text

# Tests :
# print('Function decrypt_single_byte_xor : ')
# print(decrypt_single_byte_xor('e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480'))
# # Output: 'Hi! You have found me!'
# print(decrypt_single_byte_xor('b29e9f96839085849d9085989e9f82d1889e84d199908794d197989f95d1859994d181908282869e8395d0'))
# # Output: 'Congratulations you have find the password!'
# print(decrypt_single_byte_xor('e1ded996ddd8d9c1c596c1ded7c296dfc596ded7c6c6d3d8dfd8d18996e1ded3c4d396d7db96ff89'))
# # Output: 'Who knows what is happening? Where am I?'
