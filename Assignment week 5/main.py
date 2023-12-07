def encrypt_by_add_mod(text, key):
    encrypted_text = ""

    for char in text:
        # Encrypt the character by adding the key and taking modulo 256
        encrypted_char = (ord(char) + key) % 256

        # Append the encrypted character to the result
        encrypted_text += chr(encrypted_char)

    return encrypted_text

# Examples : 
# print('Function encrypt_by_add_mod : ')
# print(encrypt_by_add_mod('Hello', 123))                                 # Output: 'Ãàççê'
# print(encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133))          # Output: 'Hello'
# print(encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246))    # Output: 'Cryptography'
# print()

################################################################################
def encrypt_xor_with_changing_key_by_prev_cipher(text, key, mode):
    if mode == 'encrypt':
        encrypted_text = ""
    
        for char in text:
            # Encrypt the character by xoring with the key
            encrypted_char = (ord(char) ^ key)

            # Append the encrypted character to the result
            encrypted_text += chr(encrypted_char)
            key = encrypted_char
        
        return encrypted_text

    elif mode == 'decrypt':
        decrypted_text = ""
        for char in text:
            # Decrypt the character by xoring with the key
            decrypted_char = (ord(char) ^ key)

            # Append the decrypted character to the result
            decrypted_text += chr(decrypted_char)
            key = ord(char)

        return decrypted_text

    else:
        raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")

# Examples : 
# print('Function encrypt_xor_with_changing_key_by_prev_cipher : ')
# print(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'))                                                                  # Output: '3V:V9'
# print(encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt')   )   # Output: 'Hello'
# print(encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt')) # Output: 'Cryptography'
# print()

################################################################################
def encrypt_xor_with_changing_key_by_prev_cipher_longer_key(text, key_list, mode):
    if len(key_list) != 4:
        raise ValueError("The key list must have 4 elements.")

    chunk_size = len(key_list)
    chunks = [text[i::chunk_size] for i in range(chunk_size)]
    encrypted_chunks = []

    for i in range(chunk_size):
        chunk_key = key_list[i]

        # Apply the previous encryption scheme on each chunk
        encrypted_chunk = encrypt_xor_with_changing_key_by_prev_cipher(chunks[i], chunk_key, mode)
        encrypted_chunks.append(encrypted_chunk)

    # Determine the maximum length among the encrypted chunks
    max_length = max(len(chunk) for chunk in encrypted_chunks)

    # Pad the encrypted chunks to match the maximum length
    padded_chunks = [chunk.ljust(max_length, '\x00') for chunk in encrypted_chunks]

    # Combine the encrypted chunks
    combined_text = ''.join([''.join(chunk) for chunk in zip(*padded_chunks)])

    # Trim any padding null characters from the end
    combined_text = combined_text.rstrip('\x00')

    return combined_text

# Example usage
key_list = [0x20, 0x44, 0x54, 0x20]
print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt'))                      # Output: 'A&7D$@P'
print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('aaabbbb', key_list, 'encrypt'))                      # Output: 'A%5B#GW'
print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg',key_list,'encrypt'), key_list,'decrypt'))     # Output: 'abcdefg'
print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('Hellobello, it will work for a long message as well',key_list,'encrypt'), 
    key_list,'decrypt'))        # Output: 'Hellobello, it will work for a long message as well'
