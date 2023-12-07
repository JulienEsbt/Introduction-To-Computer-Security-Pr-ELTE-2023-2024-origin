def encrypt_by_add_mod(plain, key):
	'''
	>>> encrypt_by_add_mod('Hello',123)
	'Ãàççê'
	>>> encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133)
	'Hello'
	>>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
	'Cryptography'
	'''
	final = []
	for curr_char in plain: 
		encoded = (ord(curr_char) + key) % 256
		final.append(chr(encoded))
	return ''.join(final)

def encrypt_xor_with_changing_key_by_prev_cipher(text, key, mode):
	'''
	>>> encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt')
	'3V:V9'
	>>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt')
	'Hello'
	>>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt')
	'Cryptography'
	'''
	if mode == 'encrypt':
		final = []
		encoded = ord(text[0]) ^ key
		final.append(chr(encoded))
		for i in range(1, len(text)):
			encoded = ord(text[i]) ^ ord(final[i-1])
			final.append(chr(encoded))
		return ''.join(final)

	elif mode == 'decrypt':
		final = []
		encoded = ord(text[0]) ^ key
		final.append(chr(encoded))
		for i in range(1, len(text)):
			encoded = ord(text[i]) ^ ord(text[i-1])
			final.append(chr(encoded))
		return ''.join(final)
	else:
		print('Wrong mode selection, please use [encrypt/decrypt]!')

def encrypt_xor_with_changing_key_by_prev_cipher_longer_key(text, key_list, mode):
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
	if mode == 'encrypt':
		chunks = []
		for i in range(0, 4):
			curr_list = text[i::4] 
			chunks.append(''.join(curr_list))
	elif mode == 'decrypt':
		pass
	else:
		print('Wrong mode selection, please use [encrypt/decrypt]!')

	final = []
	for i in range(4):
		encrypted = encrypt_xor_with_changing_key_by_prev_cipher(chunks[i], key_list[i], mode)
		final.append(encrypted)
	return ''.join(final)	

key_list = [0x20, 0x44, 0x54,0x20]
print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('AEIBFJCGDH', key_list, 'decrypt'))