def encrypt_by_add_mod(plaintext,key):
    '''
    >>> encrypt_by_add_mod('Hello',123)
    'Ãàççê'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133)
    'Hello'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
    'Cryptography'
    '''

    ret = ""
    for c in plaintext:
        ret += chr((ord(c)+key) % 256)

    return ret

def encrypt_xor_with_changing_key_by_prev_cipher(plaintext,key,mode):
    '''
    >>> encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt')
    '3V:V9'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    '''

    ret = ""
    actual_key = key
    for c in plaintext:
        actual_cipher_val = ord(c) ^ actual_key
        ret += chr(actual_cipher_val)
        if mode == 'encrypt':
            actual_key = ord(c) ^ actual_key
        else:
            actual_key = actual_cipher_val ^ actual_key

    return ret

def encrypt_xor_with_changing_key_by_prev_cipher_longer_key(plaintext, key, mode):
    '''
    >>> key_list = [0x20, 0x44, 0x54,0x20]
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt')
    'A&7D$@P'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('aaabbbb', key_list, 'encrypt')
    'A%5B#GW'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
    ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg',key_list,'encrypt'),
    ...        key_list,'decrypt')
    'abcdefg'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
    ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('Hellobello, it will work for a long message as well',key_list,'encrypt'),
    ...        key_list,'decrypt')
    'Hellobello, it will work for a long message as well'
    '''
    key_len = len(key)
    chunks = [plaintext[i::key_len] for i in range(key_len)]
    chunks_cipher = []
    for i in range(key_len):
        cipher = encrypt_xor_with_changing_key_by_prev_cipher(chunks[i], key[i], mode)
        chunks_cipher.append(cipher)

    ret = ''
    for i in range(len(plaintext)):
        which_chunk = i % len(chunks_cipher)
        character_num = i // len(chunks_cipher)
        ret += chunks_cipher[which_chunk][character_num]

    return ret