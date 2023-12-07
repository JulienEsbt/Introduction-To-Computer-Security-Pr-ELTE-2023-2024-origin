def bytes2binary(bytes_array):
    binary_string = ""
    for byte in bytes_array:
        binary_string += (bin(byte)[2:].zfill(8))
    return "".join(binary_string)

def binary2bytes(bin_string):
    bytes_array = bytearray()
    for i in range(0, len(bin_string), 8):
        byte = bin_string[i:i+8]
        bytes_array.append(int(byte, 2))
    
    return bytes(bytes_array)


def bin_xor(bin_str1, bin_str2):
    xor_str = ""
    for bit1, bit2 in zip(bin_str1, bin_str2):
        if bit1 != bit2:
            xor_str += "1"
        else:
            xor_str += "0"
    final_str=xor_str  
    while len(final_str) % 4 != 0:
        final_str="0"+ final_str
    return final_str


def permute(bit_str, table):
    bit_str_new = ""
    for position in table:
       
        bit_str_new += bit_str[position - 1]
    return bit_str_new
    
key_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63,
           55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
           
def create_DES_subkeys(key):
    

    key = permute(key, PC1)

    half = len(key) // 2

    key_1 = key[:half]
    key_2 = key[half:]

    subkeys = []
    for i in key_shifts:
        key_1 = key_1[i:] + key_1[:i]
        key_2 = key_2[i:] + key_2[:i]
        final_key = permute(key_1 + key_2, PC2)
        subkeys.append(final_key)
    return subkeys

# Tables for function f
E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

S = [
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

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]


def permute_list(substituted_result, table):
    # Permutation: Permute the result using the specified table
    permuted_result = ""
    for position in table:
        permuted_result += str(substituted_result[position - 1])

    return permuted_result

def f(half_block, subkey):
  
    expanded_block = ""
    for i in E:
        expanded_block += half_block[i - 1]

    xored_result = ""
    for a, b in zip(expanded_block, subkey):
        xored_result += str(int(a) ^ int(b))

    xored_array = []
    block = []
    counter = 0
    for i in range(0, len(xored_result)):
        counter += 1
        block.append(int(xored_result[i]))
        if counter % 6 == 0:
            xored_array.append(block)
            block = []

    substituted_result = []
  
    for i, block in enumerate(xored_array):
        row = block[0] * 2 + block[5]
        col = block[1] * 8 + block[2] * 4 + block[3] * 2 + block[4]
        s_box_value = S[i][row][col]

        for bit in format(s_box_value, '04b'):
          
            substituted_result.append(int(bit))

    permutated_res = permute_list(substituted_result, P)

    return permutated_res

# tables for encryption

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

def custom_permute(bit_str, table):
    bit_str_new = [bit_str[pos - 1] for pos in table]
    return ''.join(bit_str_new)
              
def encrypt_DES(key, message):
    
    key_binary = bytes2binary(key)
    message_binary = bytes2binary(message)

   
    subkeys = create_DES_subkeys(key_binary)

  
    message_binary = permute(message_binary, IP)

   
    left = message_binary[:32]
    right = message_binary[32:]

   
    for round_num in range(16):
    
        f_result = f(right, subkeys[round_num])

        
        substituted_result = f(right, subkeys[round_num])


        xored_left = bin_xor(left, substituted_result)

      
        left, right = right, xored_left
        
    cipher_binary = permute( right + left, IP_inverse)

    cipher_text = binary2bytes(cipher_binary)
    
    return cipher_text


from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def are_random_tests_all_passes(num_tests):

    flag = True
    
    for i in range(num_tests):
        key = get_random_bytes(8)
        message = get_random_bytes(8)

        des_cipher = DES.new(key, DES.MODE_ECB)
        des_res = des_cipher.encrypt(message)

        custom_res = encrypt_DES(key, message)

        if des_res != custom_res:
            flag = False
            break 
            
    return flag


# # Test for bytes2binary :
# print(bytes2binary(b'\x01'))          # '00000001'
# print(bytes2binary(b'\x03'))          # '00000011'
# print(bytes2binary(b'\xf0'))          # '11110000'
# print(bytes2binary(b'\xf0\x80'))      # '1111000010000000'
# print(bytes2binary(b'\x01') == '00000001' and bytes2binary(b'\x03') == '00000011' and 
#       bytes2binary(b'\xf0') == '11110000' and bytes2binary(b'\xf0\x80') == '1111000010000000')

# # Test for binary2bytes :
# print(binary2bytes('00000001'))           # b'\x01'
# print(binary2bytes('00000011'))           # b'\x03'
# print(binary2bytes('11110000'))           # b'\xf0'
# print(binary2bytes('1111000010000000'))   # b'\xf0\x80'
# print(binary2bytes('00000001') == b'\x01' and binary2bytes('00000011') == b'\x03' and 
#       binary2bytes('11110000') == b'\xf0' and binary2bytes('1111000010000000') == b'\xf0\x80')

# # Test for bin_xor :
# print(bin_xor('1011', '0000'))              # '1011'
# print(bin_xor('1', '0000'))                 # '0001'
# print(bin_xor('1101', '1011'))              # '0110'
# print(bin_xor('10101010', '01010101'))      # '11111111'
# print(bin_xor('1011', '0000') == '1011' and bin_xor('1', '0000') == '0001' and 
#       bin_xor('1101', '1011') == '0110' and bin_xor('10101010', '01010101') == '11111111')

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

# # Test for f :
# print(f('11110000101010101111000010101010','000110110000001011101111111111000111000001110010'))  # 00100011010010101010100110111011
# print(f('11110000101010101111000010101010','000110110000001011101111111111000111000001110010') == '00100011010010101010100110111011')

# # Test for encrypt_DES :
# print(encrypt_DES(b'\x13\x34\x57\x79\x9b\xbc\xdf\xf1', b'\x01\x23\x45\x67\x89\xab\xcd\xef')) # b'\x85\xe8\x13T\x0f\n\xb4\x05'
# print(encrypt_DES(b'\x13\x34\x57\x79\x9b\xbc\xdf\xf1', b'\x01\x23\x45\x67\x89\xab\xcd\xef') == b'\x85\xe8\x13T\x0f\n\xb4\x05')

# # Test for are_random_tests_all_passes :
# print(are_random_tests_all_passes(1000)) # True