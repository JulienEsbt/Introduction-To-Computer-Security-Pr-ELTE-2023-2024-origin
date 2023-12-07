import base64 

def hex2bin(number):
    '''
    >>> hex2bin('f')
    '1111'
    >>> hex2bin('5')
    '101'
    >>> hex2bin('1')
    '1'
    '''
    return format(int(number, base=16), "b")

def bin2hex(number):
    '''
    >>> bin2hex('1111')
    'f'
    >>> bin2hex('100001')
    '21'
    >>> bin2hex('1')
    '1'
    '''
    return hex(int(number, base=2))[2:]

def fillupbyte(binary):
    '''
    >>> fillupbyte('011')
    '00000011'
    >>> fillupbyte('1')
    '00000001'
    >>> fillupbyte('10111')
    '00010111'
    >>> fillupbyte('11100111')
    '11100111'
    >>> fillupbyte('111001111')
    '0000000111001111'
    '''
    i = 1
    while len(binary) % 8 != 0:
        binary = binary.rjust(i, "0")
        i += 1
    return binary

def int2base64(number):
    '''
    >>> int2base64(0x61)
    'YQ=='
    >>> int2base64(0x78)
    'eA=='
    '''
    enc = base64.b64encode(bytes([number]))
    return enc.decode('utf-8')

def hex2base64(number): 
    '''
    >>> hex2base64('61')
    'YQ=='
    >>> hex2base64('123456789abcde')
    'EjRWeJq83g=='
    '''

    #Tried doing it step-by-step, got stuck at converting 6 bits into base64
    '''
    bin = hex2bin(number)
    padded = fillupbyte(bin)
    i = 1
    while len(padded) % 6 != 0:
        padded = padded.ljust(i, "0")
        i += 1
    print(padded)
    encoded = ""
    for i in range(0, len(padded), 6): 
        #bits = padded[i:i+6]
        #print(base64.b64encode(bytes([int(bits, 2)])))
        #encoded.append()
    '''
    return base64.b64encode(bytes.fromhex(number)).decode()