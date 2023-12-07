from Crypto.Cipher import AES

def decrypt_aes_ecb(encrypted_message, key):
    '''Decrypts the provided encrypted message using AES ECB mode with the provided key.'''
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(encrypted_message)

# # Test for decrypt_aes_ecb :
# key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])   
# print(decrypt_aes_ecb(bytes([215, 221, 59, 138, 96, 94, 155, 69, 52, 90, 212, 108, 49, 65, 138, 179]), key))        # b'lovecryptography'
# print(decrypt_aes_ecb(bytes([147, 140, 44, 177, 97, 209, 42, 239, 152, 124, 241, 175, 202, 164, 183, 18]), key))    # b'!!really  love!!'

####################################################################################################

def xor_byte_arrays(input1, input2):
    '''XORs two byte arrays.'''
    # Figuring out the longest array to match the lengths
    max_len = max(len(input1), len(input2))

    # Padding the arrays to make them equal in length.
    input1_padded = input1.rjust(max_len, bytes([0]))
    input2_padded = input2.rjust(max_len, bytes([0]))

    # Performing XOR operation
    return bytes([b1 ^ b2 for b1, b2 in zip(input1_padded, input2_padded)])

# # Test for xor_byte_arrays :
# print(xor_byte_arrays(bytes([1, 2, 3, 4]), bytes([2, 3, 4, 5])))                                # b'\x03\x01\x07\x01'
# print(xor_byte_arrays(bytes([1, 2, 3, 4]), bytes([])))                                          # b'\x01\x02\x03\x04'
# print(xor_byte_arrays(bytes([1, 2, 3, 4]), bytes([1, 2])))                                      # b'\x01\x02\x02\x06'
# print(xor_byte_arrays(bytes([1, 2, 4, 8, 16, 32, 64, 128]), bytes([1, 1, 1, 1, 1, 1, 1, 1])))   # b'\x00\x03\x05\t\x11!A\x81'
# print(b'\x00\x03\x05\t\x11!A\x81' == bytes([0,3,5,9,17,33,65,129]))                             # True
# print(b'\x01\x02\x03\x04' == bytes([1,2,3,4]))                                                  # True

####################################################################################################

def decrypt_aes_cbc_with_ecb(ciphertext, key, iv):
    ''' Decrypts AES-encrypted data in CBC mode using our homemade ECB function.'''
    block_size = 16  # AES block size in bytes
    decrypted_message = b''

    # Decrypting block by block
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        decrypted_block = decrypt_aes_ecb(block, key)

        # XOR with IV for the first block, or the previous ciphertext block for subsequent blocks
        if i == 0:
            decrypted_message += xor_byte_arrays(decrypted_block, iv)
        else:
            decrypted_message += xor_byte_arrays(decrypted_block, ciphertext[i-block_size:i])

    return decrypted_message

# # Test for decrypt_aes_cbc_with_ecb :
# key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
# iv = bytes([241, 147, 66, 129, 194, 34, 37, 51, 236, 69, 188, 205, 64, 140, 244, 204])
# print(decrypt_aes_cbc_with_ecb(bytes([255, 18, 67, 115, 172, 117, 242, 233, 246, 69, 81, 156, 52, 154, 123, 171]), key, iv))    # b'hello world 1234'
# print(decrypt_aes_cbc_with_ecb(bytes([171, 218, 160, 96, 193, 134, 73, 81, 221, 149, 19, 180, 31, 247, 106, 64]), key, iv))     # b'lovecryptography'
# print(decrypt_aes_cbc_with_ecb(bytes([171, 218, 160, 96, 193, 134, 73, 81, 221, 149, 19, 180, 31, 247, 106, 64] * 2), key, iv)) # b'lovecryptography6&\x94\x84`\xd6\x15\x12E\xbf\xc8\x0b>\x0b\xf6\xf5'

####################################################################################################

def encrypt_aes_ecb(plaintext, key):
    ''' Encrypts the provided plaintext using AES ECB mode with the provided key.'''
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plaintext)

def pad_plaintext(plaintext, block_size):
    ''' Pads the provided plaintext to be a multiple of the block size.'''
    padding_length = (block_size - len(plaintext) % block_size) % block_size
    return plaintext + bytes([padding_length] * padding_length)

def encrypt_aes_cbc_with_ecb(plaintext, key, iv):
    ''' Encrypts the provided plaintext using the previous function that we built, with the provided key and iv.'''
    block_size = AES.block_size
    ciphertext = b''
    previous_block = iv

    # Padding the plaintext
    padded_plaintext = pad_plaintext(plaintext, block_size)

    # Encrypting block by block
    for i in range(0, len(padded_plaintext), block_size):
        block = padded_plaintext[i:i+block_size]
        xored_block = xor_byte_arrays(block, previous_block)
        encrypted_block = encrypt_aes_ecb(xored_block, key)
        ciphertext += encrypted_block
        previous_block = encrypted_block

    return ciphertext

# # Test for encrypt_aes_cbc_with_ecb :
# key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
# iv = bytes([241, 147, 66, 129, 194, 34, 37, 51, 236, 69, 188, 205, 64, 140, 244, 204])
# print(encrypt_aes_cbc_with_ecb(b'hello world 1234', key, iv))       # b'\xff\x12Cs\xacu\xf2\xe9\xf6EQ\x9c4\x9a{\xab'
# print(encrypt_aes_cbc_with_ecb(b'lovecryptography', key, iv))       # b'\xab\xda\xa0`\xc1\x86IQ\xdd\x95\x13\xb4\x1f\xf7j@'
