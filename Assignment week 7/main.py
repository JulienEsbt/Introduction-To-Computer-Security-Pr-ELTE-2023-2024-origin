from Crypto.Cipher import AES

def decrypt_aes(ciphertext, key, iv):
    ''' Decrypts the provided ciphertext using AES mode with the provided key and IV.'''
    # Create an AES cipher object with the provided key and AES mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    output = cipher.decrypt(ciphertext)

    return output


def bit_permutation(input_str, order):
    ''' Performs a bit permutation on the provided input string using the provided order.
    # Personal : The order is a list of integers that specify the new position of each bit in the input string. I was doing it the other way around at first.'''
    output_list = ['0'] * len(order)

    # Perform the permutation
    for i, pos in enumerate(order):
        output_list[i] = input_str[pos - 1]

    # Convert the list to a string
    output_str = ''.join(output_list)

    return output_str


def left_shift_rot(binary_str, steps=1):
    ''' Performs a left rotation on the provided binary string by the provided number of steps.'''
    # Calculate the effective number of steps by taking the modulo of the length
    steps %= len(binary_str)

    # Perform the left rotation
    output = binary_str[steps:] + binary_str[:steps]

    return output


def PKCS7_pad(text, block_size):
    ''' Pads the provided text with PKCS7 padding to the provided block size.'''
    # Check that the block size is valid
    if block_size < 1 or block_size > 255:
        raise ValueError("Block size must be between 1 and 255")

    # Calculate the padding length
    padding_length = block_size - len(text) % block_size

    # Create the padding
    padding = chr(padding_length) * padding_length

    return text + padding


# # Tests for decrypt_aes : 
# key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
# iv = bytes([241, 147, 66, 129, 194, 34, 37, 51, 236, 69, 188, 205, 64, 140, 244, 204])
# print(decrypt_aes(bytes([255, 18, 67, 115, 172, 117, 242, 233, 246, 69, 81, 156, 52, 154, 123, 171]), key, iv))   
#     # Output: b'hello world 1234'
# print(decrypt_aes(bytes([171, 218, 160, 96, 193, 134, 73, 81, 221, 149, 19, 180, 31, 247, 106, 64]), key, iv))    
#     # Output: b'lovecryptography'

# # Tests for bit_permutation :
# print(bit_permutation("101", [1, 2, 3]))                        # Output: '101'
# print(bit_permutation("101", [3, 2, 1]))                        # Output: '101'
# print(bit_permutation("101", [1, 3, 2]))                        # Output: '110'
# print(bit_permutation("101", [3, 2, 1]))                        # Output: '101'
# print(bit_permutation("1010", [3, 4, 1, 2]))                    # Output: '1010'
# print(bit_permutation("1010", [1, 3, 2, 4]))                    # Output: '1100'
# print(bit_permutation("11110000", [5, 6, 7, 8, 1, 2, 3, 4]))    # Output: '00001111'
# print(bit_permutation("0001001100110100010101110111100110011011101111001101111111110001",[57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11,  3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]))
# # Output: '11110000110011001010101011110101010101100110011110001111'

# # Tests for left_shift_rot :
# print(left_shift_rot('010'))                # Output: '100'
# print(left_shift_rot('111'))                # Output: '111'
# print(left_shift_rot('1010111001'))         # Output: '0101110011'
# print(left_shift_rot('0101110011'))         # Output: '1011100110'
# print(left_shift_rot('1010111001', 2))      # Output: '1011100110'
# print(left_shift_rot('0001', 3))            # Output: '1000'

# # Tests for PKCS7_pad :
# print(PKCS7_pad('hello', 88))                   # Output: 'helloSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'
# print(PKCS7_pad('', 0x70))                      # Output: 'pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp'
# print(PKCS7_pad('a', 0x70))                     # Output: 'aooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'
# print(PKCS7_pad('abc', 0x70))                   # Output: 'abcmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# print(PKCS7_pad('hello, how are you?', 55))     # Output: 'hello, how are you?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
# print(PKCS7_pad('hello, how are you?', 67))     # Output: 'hello, how are you?000000000000000000000000000000000000000000000000'
