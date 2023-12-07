# --------------------------------
# DES Matrices and Tables
# --------------------------------

# Tables for key generation
key_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63,
       55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

# Tables for encryption
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

IP_inverse = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

# Tables for function f
# Expansion table
E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22,
    23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# S-boxes
S = \
[
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# Permutation table
P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

# --------------------------------
# Function for Assignment week 10
# --------------------------------


def bytes2binary(byte_array):
    '''Converts an array of bytes to a string containing the binary representation.'''
    return ''.join(f'{byte:08b}' for byte in byte_array)

# # Test for bytes2binary :
# print(bytes2binary(b'\x01'))          # '00000001'
# print(bytes2binary(b'\x03'))          # '00000011'
# print(bytes2binary(b'\xf0'))          # '11110000'
# print(bytes2binary(b'\xf0\x80'))      # '1111000010000000'
# print(bytes2binary(b'\x01') == '00000001' and bytes2binary(b'\x03') == '00000011' and 
#       bytes2binary(b'\xf0') == '11110000' and bytes2binary(b'\xf0\x80') == '1111000010000000')

####################################################################################################

def binary2bytes(binary_str):
    '''Converts a string containing the binary representation to an array of bytes.'''
    return bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))

# # Test for binary2bytes :
# print(binary2bytes('00000001'))           # b'\x01'
# print(binary2bytes('00000011'))           # b'\x03'
# print(binary2bytes('11110000'))           # b'\xf0'
# print(binary2bytes('1111000010000000'))   # b'\xf0\x80'
# print(binary2bytes('00000001') == b'\x01' and binary2bytes('00000011') == b'\x03' and 
#       binary2bytes('11110000') == b'\xf0' and binary2bytes('1111000010000000') == b'\xf0\x80')

####################################################################################################

def bin_xor(bin_str1, bin_str2):
    '''Performs a binary XOR operation on two binary strings.'''
    # Pad the shorter string with leading zeros
    max_len = max(len(bin_str1), len(bin_str2))
    bin_str1 = bin_str1.rjust(max_len, '0')
    bin_str2 = bin_str2.rjust(max_len, '0')

    # Perform XOR operation
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bin_str1, bin_str2))

# # Test for bin_xor :
# print(bin_xor('1011', '0000'))              # '1011'
# print(bin_xor('1', '0000'))                 # '0001'
# print(bin_xor('1101', '1011'))              # '0110'
# print(bin_xor('10101010', '01010101'))      # '11111111'
# print(bin_xor('1011', '0000') == '1011' and bin_xor('1', '0000') == '0001' and 
#       bin_xor('1101', '1011') == '0110' and bin_xor('10101010', '01010101') == '11111111')

####################################################################################################

def permute(binary_str, array):
    '''Permute the key using the provided array.'''
    return ''.join(binary_str[i - 1] for i in array)

def left_shift(binary_str, shifts):
    '''Perform left circular shift.'''
    return binary_str[shifts:] + binary_str[:shifts]

def create_DES_subkeys(key):
    '''Generate 16 subkeys for DES encryption from the initial key.'''
    # Initial key permutation (PC-1)
    key = permute(key, PC1)

    # Splitting
    left = key[:28]
    right = key[28:]

    # Subkey generation
    subkeys = []
    for shift in key_shifts:
        left = left_shift(left, shift)
        right = left_shift(right, shift)

        # Permutation 2 (PC-2)
        key_comb = left + right
        subkeys.append(permute(key_comb, PC2))

    return subkeys

# # Test for create_DES_subkeys :
# print(create_DES_subkeys('0001001100110100010101110111100110011011101111001101111111110001') == 
#       ['000110110000001011101111111111000111000001110010', '011110011010111011011001110110111100100111100101', 
#        '010101011111110010001010010000101100111110011001', '011100101010110111010110110110110011010100011101', 
#        '011111001110110000000111111010110101001110101000', '011000111010010100111110010100000111101100101111', 
#        '111011001000010010110111111101100001100010111100', '111101111000101000111010110000010011101111111011', 
#        '111000001101101111101011111011011110011110000001', '101100011111001101000111101110100100011001001111', 
#        '001000010101111111010011110111101101001110000110', '011101010111000111110101100101000110011111101001', 
#        '100101111100010111010001111110101011101001000001', '010111110100001110110111111100101110011100111010', 
#        '101111111001000110001101001111010011111100001010', '110010110011110110001011000011100001011111110101'])

# --------------------------------
# Function for Big Assignment
# --------------------------------

def f(input, key):
    '''Implement the core f function of the simple DES encryption scheme.'''
    # Expansion permutation
    input = permute(input, E)

    # XOR with key
    input = bin_xor(input, key)

    # S-boxes
    B = [input[i:i + 6] for i in range(0, len(input), 6)]
    B = [S[i][int(B[i][0] + B[i][-1], 2)][int(B[i][1:-1], 2)] for i in range(len(B))]
    input = ''.join(f'{b:04b}' for b in B)

    # Permutation
    input = permute(input, P)

    return input

# # Test for f :
# print(f('11110000101010101111000010101010','000110110000001011101111111111000111000001110010'))  # 00100011010010101010100110111011
# print(f('11110000101010101111000010101010','000110110000001011101111111111000111000001110010') == '00100011010010101010100110111011')

####################################################################################################

def encrypt_DES(key, message):
    '''Encrypts the provided message using the provided key.'''
    # Convert key and message from bytes to binary string
    key_binary = bytes2binary(key)
    message_binary = bytes2binary(message)
    # print('key_binary : ', key_binary)
    # print('message_binary : ', message_binary)

    # Generate subkeys
    subkeys = create_DES_subkeys(key_binary)
    # print('subkeys : ', subkeys)

    # Initial permutation
    message_binary = permute(message_binary, IP)
    # print('message_binary : ', message_binary)

    # Split message into left and right halves
    left = message_binary[:32]
    right = message_binary[32:]
    # print('left : ', left, 'right : ', right)

    # 16 rounds
    for i in range(16):
        left, right = right, bin_xor(left, f(right, subkeys[i]))
        # print('left : ', left, 'right : ', right)

    # Combine halves and apply final permutation
    combined = right + left  # Note: R and L are swapped
    # print('combined : ', combined)
    cipher_binary = permute(combined, IP_inverse)
    # print('cipher_binary : ', cipher_binary)

    # Convert binary string to bytes
    cipher_text = binary2bytes(cipher_binary)
    # print('cipher_text : ', cipher_text)
    return cipher_text

# # Test for encrypt_DES :
# print(encrypt_DES(b'\x13\x34\x57\x79\x9b\xbc\xdf\xf1', b'\x01\x23\x45\x67\x89\xab\xcd\xef')) # b'\x85\xe8\x13T\x0f\n\xb4\x05'
# print(encrypt_DES(b'\x13\x34\x57\x79\x9b\xbc\xdf\xf1', b'\x01\x23\x45\x67\x89\xab\xcd\xef') == b'\x85\xe8\x13T\x0f\n\xb4\x05')

####################################################################################################

from Crypto.Cipher import DES
import os

def are_random_tests_all_passes(num_tests):
    '''Runs the DES algorithm in ECB mode from the Crypto.cipher library and my encryption algorithm to see if the results match.'''
    for _ in range(num_tests):
        # Generate a random key and message
        key = os.urandom(8)
        message = os.urandom(8)

        # Run the DES algorithm in ECB mode from the Crypto.cipher library
        cipher = DES.new(key, DES.MODE_ECB)
        expected_cipher_text = cipher.encrypt(message)

        # Run my encryption algorithm with the same key and message
        actual_cipher_text = encrypt_DES(key, message)

    return actual_cipher_text == expected_cipher_text

# # Test for are_random_tests_all_passes :
# print(are_random_tests_all_passes(1000)) # True