# Code from previous week that I need for this week :

def hex2bin(hex_value):
    '''
    >>> hex2bin('f')
    '1111'
    >>> hex2bin('1')
    '1'
    '''
    return bin(int(hex_value, 16))[2:]


def bin2hex(binary):
    '''
    >>> bin2hex('1111')
    'f'
    >>> bin2hex('1')
    '1'
    '''
    return hex(int(binary, 2))[2:]