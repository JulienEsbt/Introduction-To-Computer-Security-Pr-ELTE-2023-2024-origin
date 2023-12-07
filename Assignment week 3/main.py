def hex2bin(hex_string):
    '''Write a function without any library that converts a string, containing the hex representation of a number,
    to binary.'''

    # Define the mapping of hex characters to their decimal values
    hex_map = {
        '0': '0', '1': '1', '2': '10', '3': '11',
        '4': '100', '5': '101', '6': '110', '7': '111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    # Convert the hex string to binary
    binary_string = ''
    for char in hex_string:
        binary_string += hex_map[char.upper()]

    return binary_string


# print(hex2bin('f'))
# print(hex2bin('5'))
# print(hex2bin('1'))

######################################################################
def bin2hex(binary_string):
    '''Write a function that converts a string, containing binary representation of a number, to hexadecimal format.'''

    # Define the mapping of binary characters to their hex values
    bin_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }

    # Convert the binary string to hex
    hex_string = ''
    while len(binary_string) % 4 != 0:
        binary_string = '0' + binary_string

    for i in range(0, len(binary_string), 4):
        hex_string += bin_map[binary_string[i:i + 4]]

    return hex_string.lower()


# print(bin2hex('1111'))
# print(bin2hex('100001'))
# print(bin2hex('1'))

######################################################################
def fillupbyte(binary_string):
    '''Create a function that pad a string, containing binary representation of a number, to get a string length that can be divided by 8.'''

    while len(binary_string) % 8 != 0:
        binary_string = '0' + binary_string

    return binary_string


# print(fillupbyte('011'))
# print(fillupbyte('1'))
# print(fillupbyte('10111'))
# print(fillupbyte('11100111'))
# print(fillupbyte('111001111'))

######################################################################
def int2base64(int):
    '''Write a function that converts an integer to base64 format.'''

    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_result = ""

    while int > 0:
        # Extract the last 6 bits from the integer
        bits = int & 0b111111

        # Convert the 6 bits to a base64 character
        base64_result = base64_chars[bits] + base64_result

        # Right-shift the integer by 6 bits
        int >>= 6

    # If the resulting base64 string is not a multiple of 4 characters, add padding '='
    padding = (4 - len(base64_result) % 4) % 4
    base64_result += '=' * padding

    print('Function not working, still need to correct it')
    return base64_result


# print(int2base64(0x61))
# print(int2base64(0x78))

######################################################################
def hex2base64(hex_string):
    '''Create in python a hex2base64 function that converts, a string containing hex code, to base64 encoding without using any library.'''

    # Define the mapping of hex characters to their decimal values
    hex_map = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'a': 10, 'b': 11,
        'c': 12, 'd': 13, 'e': 14, 'f': 15
    }

    # Initialize variables
    binary_string = ''
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # Convert hex to binary
    for hex_char in hex_string:
        if hex_char in hex_map:
            binary_string += format(hex_map[hex_char], '04b')
        else:
            raise ValueError("Invalid hex character: {}".format(hex_char))

    # Pad the binary string to be a multiple of 6 bits
    while len(binary_string) % 6 != 0:
        binary_string += '0'

    # Convert binary to base64
    base64_string = ''
    while binary_string:
        base64_index = int(binary_string[:6], 2)
        base64_string += base64_chars[base64_index]
        binary_string = binary_string[6:]

    # Add padding characters if necessary
    while len(base64_string) % 4 != 0:
        base64_string += '='

    return base64_string


# print(hex2base64('61'))
# print(hex2base64('123456789abcde'))
