def hex2string(number): 
    '''
    >>> hex2string('61')
    'a'
    >>> hex2string('776f726c64')
    'world'
    >>> hex2string('68656c6c6f')
    'hello'
    '''
    return bytes.fromhex(number).decode(errors="ignore")

def string2hex(string): 
    '''
    >>> string2hex('a')
    '61'
    >>> string2hex('hello')
    '68656c6c6f'
    >>> string2hex('world')
    '776f726c64'
    >>> string2hex('foo')
    '666f6f'
    '''
    return string.encode('utf-8').hex()

def hex_xor(n1, n2):
    '''
    >>> hex_xor('0aabbf11','12345678')
    '189fe969'
    >>> hex_xor('12cc','12cc')
    '0000'
    >>> hex_xor('1234','2345')
    '3171'
    >>> hex_xor('111','248')
    '359'
    >>> hex_xor('8888888','1234567')
    '9abcdef'
    '''
    n = hex(int(n1, 16) ^ int(n2, 16))[2:]
    return n.zfill(len(n1))

def encrypt_single_byte_xor(input, key):
    '''
    >>> encrypt_single_byte_xor('aaabbccc','00')
    'aaabbccc'
    >>> encrypt_single_byte_xor(string2hex('hello'),'aa')
    'c2cfc6c6c5'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('hello'),'aa'),'aa'))
    'hello'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('Encrypt and decrypt are the same'),'aa'),'aa'))
    'Encrypt and decrypt are the same'
    '''
    long_key = key * (len(input) // len(key))
    return hex_xor(input, long_key)

def count_letters(string):
    c = 0
    for curr_char in string:
        if(curr_char.isalpha() or curr_char == " "):
            c += 1
    return c

def decrypt_single_byte_xor(input):
    '''
    >>> decrypt_single_byte_xor('e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480')
    'Hi! You have found me!'
    >>> decrypt_single_byte_xor('b29e9f96839085849d9085989e9f82d1889e84d199908794d197989f95d1859994d181908282869e8395d0')
    'Congratulations you have find the password!'
    '''
    bytes = [hex(x)[2:].zfill(2) for x in range(256)]
    best_guess = ""
    best_nof_letters = 0
    for curr_key in bytes:
        decrypted = hex2string(encrypt_single_byte_xor(input, curr_key))
        nof_letters = count_letters(decrypted)
        if nof_letters > best_nof_letters:
            best_guess = decrypted
            best_nof_letters = nof_letters
    return best_guess