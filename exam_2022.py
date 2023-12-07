# Implement a function that converts a 2-length string to integer (separately the two character as ascii character).
# The first character will be the most significant byte of the output integer.
# The second character will be the least significant byte.
# Check the doctest examples.
# Hint: use ord separately for the two characters of the parameter.
def two_character_to_int(two_character_string):
    '''
    >>> hex(two_character_to_int('aa'))
    '0x6161'
    >>> two_character_to_int('aa')
    24929
    >>> hex(two_character_to_int('ab'))
    '0x6162'
    >>> two_character_to_int('ab')
    24930
    >>> hex(two_character_to_int('Ab'))
    '0x4162'
    >>> two_character_to_int('Ab')
    16738
    >>> hex(two_character_to_int('&v'))
    '0x2676'
    >>> hex(two_character_to_int('~ '))
    '0x7e20'
    '''
    two_character_string = two_character_string.encode('ascii')
    return two_character_string[0] * 256 + two_character_string[1]

print(hex(two_character_to_int('ab')))

# Create a function that converts an integer (that can be at most 2 byte sized),
# to ascii characters separately by bytes.
# Every byte of the input integer has to be converted to ascii separately.
# Hint: You can convert it directly by mod and div.
# Hint: You can convert to hex and use the 1,2 bytes and then the 3,4th bytes.
def two_byte_int_to_string(two_byte_int):
    '''
    >>> two_byte_int_to_string(0x6161)
    'aa'
    >>> two_byte_int_to_string(0x6162)
    'ab'
    >>> two_byte_int_to_string(0x4162)
    'Ab'
    >>> two_byte_int_to_string(0x2676)
    '&v'
    >>> two_byte_int_to_string(0x7e20)
    '~ '
    '''
    return ''

# Implement a function that encrypts an input string by a two byte sized integer key with xor.
# In this case you have two byte blocks and encrypt all the 2 byte sized blocks by the same key.
# If the message is odd length, then pad it from the right with zero, and cut the resulting cipher to the original length.
def encpryt_xor_by_two_byte_sized_key(message, key):
    '''
    >>> encpryt_xor_by_two_byte_sized_key('abcdefghij{}',0x2020)
    'ABCDEFGHIJ[]'
    >>> encpryt_xor_by_two_byte_sized_key('ABCDEFGHIJ{}',0x2020)
    'abcdefghij[]'
    >>> encpryt_xor_by_two_byte_sized_key('ABCDEFGHIJL',0x2020)
    'abcdefghijl'
    >>> encpryt_xor_by_two_byte_sized_key('ABCDEFG',0x0101)
    '@CBEDGF'
    >>> encpryt_xor_by_two_byte_sized_key('0123456789',0x1040)
    ' q"s$u&w(y'
    '''
    return ''


# Create an improved version of the previous function by change the key block by block by squaring the key and modulo by 2**16.
# The first block (2 byte) will be encrypted similarly as in the previous task,
# but the second block's key will be calculated by the first block's key by squaring and modulo by 2**16 and so on.
# For example if the first block's key is 0x0002, then the second block will be encrypted by the 0x0004 key, the third by 0x0010 and so on
def encpryt_xor_by_two_byte_sized_key_changing_key(message, key):
    '''
    >>> encpryt_xor_by_two_byte_sized_key_changing_key('abcdefghij{}',0x2020) #block keys: 0x2020, 0x0400, 0x0000, 0x0000
    'ABgdefghij{}'
    >>> encpryt_xor_by_two_byte_sized_key_changing_key('ABCDEFG',0x0101) #block keys: 0x0101, 0x0201, 0x0401, 0x0801
    '@CAEAGO'
    >>> encpryt_xor_by_two_byte_sized_key_changing_key('0123456789',0x1040) # block keys: 0x1040, 0x1000, 0x0000
    ' q"3456789'
    >>> encpryt_xor_by_two_byte_sized_key_changing_key('APPLE',0x0011) # block keys: 0x0011, 0x0121, 0x4641
    'AAQm\\x03'
    >>> encpryt_xor_by_two_byte_sized_key_changing_key(encpryt_xor_by_two_byte_sized_key_changing_key('APPLE',0x0011),0x0011)
    'APPLE'
    >>> encpryt_xor_by_two_byte_sized_key_changing_key(encpryt_xor_by_two_byte_sized_key_changing_key('purple......???!!!',0x1234),0x1234)
    'purple......???!!!'
    >>> encpryt_xor_by_two_byte_sized_key_changing_key(encpryt_xor_by_two_byte_sized_key_changing_key('test: ?!136/--*+~~2+!%/=();>*#>*',0x644f),0x644f)
    'test: ?!136/--*+~~2+!%/=();>*#>*'
    '''
    return ''