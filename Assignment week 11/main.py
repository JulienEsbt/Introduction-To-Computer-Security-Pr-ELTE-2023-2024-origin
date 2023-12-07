import hashlib
import itertools

def sha256(input_string):
    # Create a new SHA256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the input string, encoded to bytes
    hash_object.update(input_string.encode())

    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

# # ----- Test sha256 function :
# print(sha256('I') == 'a83dd0ccbffe39d071cc317ddf6e97f5c6b1c87af91919271f9fa140b0508c6c')
# print(sha256('love') == '686f746a95b6f836d7d70567c302c3f9ebb5ee0def3d1220ee9d4e9f34f5e131')
# print(sha256('crypto') == 'da2f073e06f78938166f247273729dfe465bf7e46105c13ce7cc651047bf0ca4')

def authenticate(username, password):
    # Simulated database with SHA256 hashed passwords
    users = {
        'admin': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', # sha256('admin')
        'user': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',  # sha256('hello')
    }

    # Hash the input password
    hashed_password = sha256(password)

    # Check if the username exists and the password matches
    return users.get(username) == hashed_password

# # ----- Test authenticate function :
# print(authenticate('admin', 'admin') == True)
# print(authenticate('admin', 'admin2') == False)
# print(authenticate('user', 'hello') == True)
# print(authenticate('user', 'helo') == False)

def hack_sha256_fixed_size(hash_value, length):
    chars = 'abcdefghijklmnopqrstuvwxyz'

    # Generate all possible combinations of characters of the given length
    for combo in itertools.product(chars, repeat=length):
        # Join the characters to form a word
        word = ''.join(combo)

        # Hash the word and compare with the given hash
        if sha256(word) == hash_value:
            return word

    return None

# # ----- Test hack_sha256_fixed_size function :
# print(hack_sha256_fixed_size('8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 5) == 'admin')
# print(hack_sha256_fixed_size('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', 5) == 'hello')
# print(hack_sha256_fixed_size('a819d7cd38e9101be2e496298e8bf426ce9cdf78d2af35ddf44c6ad25d50158b', 5) == 'crypt')
# print(hack_sha256_fixed_size('688787d8ff144c502c7f5cffaafe2cc588d86079f9de88304c26b0cb99ce91c6', 3) == 'asd')
# print(hack_sha256_fixed_size('7ec658e98073955c48314d0146593497a163d79f4e1dfea4bab03b79af227214', 4) == 'elte')

def hack_sha256(hash_value):
    for length in range(1, 11):  # Iterate through lengths from 1 to 10
        result = hack_sha256_fixed_size(hash_value, length)
        if result is not None:
            return result
    return None

# # ----- Test hack_sha256 function :
# print(hack_sha256('8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918') == 'admin')
# print(hack_sha256('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824') == 'hello')
# print(hack_sha256('a819d7cd38e9101be2e496298e8bf426ce9cdf78d2af35ddf44c6ad25d50158b') == 'crypt')
# print(hack_sha256('688787d8ff144c502c7f5cffaafe2cc588d86079f9de88304c26b0cb99ce91c6') == 'asd')
# print(hack_sha256('7ec658e98073955c48314d0146593497a163d79f4e1dfea4bab03b79af227214') == 'elte')

# Longer examples
# So here, I found a website (https://crackstation.net) that has a database of hashed passwords. I tried with the hashes that you 
# provided and there was an answer, so I downloaded the database and used it to try to find out by myself. So I wrote this function :
# hack_sha256_with_database, that takes a hash and returns the password if it is in the database, and None otherwise.
# I also tried with a lighter database (crackstation-human-only.txt) that only contains passwords that are made of letters and numbers, 
# and it worked too, but only for the first and the thrid hashes and passwords that you provided. I think that the second one is not in
# the database it contains a space, which is not allowed in this lighter database.
# If you want to try it, you need to download the database and change the path in the function.

def hack_sha256_with_database(hash_to_crack):
    # To solve encoding problem that I had with the database
    encodings = ['utf-8', 'latin-1', 'utf-16']
    for encoding in encodings:
        try:
            # with open('/Users/julienesbt/Documents/Etudes/Master/M2/S1/Introduction to Computer Security/Practices/Assignment week 11/crackstation.txt', 'r', encoding=encoding) as file:
            with open('/Users/julienesbt/Documents/Etudes/Master/M2/S1/Introduction to Computer Security/Practices/Assignment week 11/crackstation-human-only.txt', 'r', encoding=encoding) as file:
                for line in file:
                    line = line.strip()  # Remove any trailing newline characters
                    if sha256(line) == hash_to_crack:
                        return line  # Return the plaintext password
            break  # Break the loop if file is successfully read
        except UnicodeDecodeError:
            continue  # Try the next encoding if current one fails
    return None  # Return None if no match is found

# # ----- Test hack_sha256_with_database function :
# print(hack_sha256_with_database('e06554818e902b4ba339f066967c0000da3fcda4fd7eb4ef89c124fa78bda419'))    # 'cryptography'
# print(hack_sha256_with_database('8aa261cbc05ad6a49bea91521e51c8b979aa78215b8defd51fc0cebecc4d5c96'))    # 'romeo and juliet'
# print(hack_sha256_with_database('f2b826b18b9de86628dd9b798f3cb6cfd582fb7cee4ea68489387c0b19dc09c1'))    # 'vulnerable'

def authenticate_with_pepper(username, password):
    pepper_prefix = 'this_can_help_to_confuse_the_attacker_'

    # Database with pepper-prefixed password hashes
    users_with_pepper = {
        'admin': {'passwordHash': '89e6b5ed137e3864d99ec9b421cf6f565d611f4c2b98e31a7d353d63aa748e9c'}, # sha256('this_can_help_to_confuse_the_attacker_admin')
        'user': {'passwordHash': '6dc765830e675d5fa4a9afb248be09a0407f6353d44652fd9b36038884a76323'},  # sha256('this_can_help_to_confuse_the_attacker_hello')
    }

    # Hash the pepper-prefixed password
    hashed_password = sha256(pepper_prefix + password)

    # Check if the username exists and the password matches
    return users_with_pepper.get(username, {}).get('passwordHash') == hashed_password

# # ----- Test authenticate_with_pepper function :
# print(authenticate_with_pepper('admin', 'admin') == True)
# print(authenticate_with_pepper('admin', 'admin2') == False)
# print(authenticate_with_pepper('user', 'hello') == True)
# print(authenticate_with_pepper('user', 'helo') == False)

def authenticate_with_pepper_and_salt(username, password):
    pepper_prefix = 'this_can_help_to_confuse_the_attacker_'

    # Database with pepper-prefixed and salted password hashes
    users_with_pepper_and_salt = {
        'admin': {'passwordHash': 'd3eab7f4d6974f1db32b9cd9923fce9b434b28dc229b6582b845f1fca770d9f7', 'salt': "5294976873732394418"}, # sha256('this_can_help_to_confuse_the_attacker_admin5294976873732394418')
        'user': {'passwordHash': '976c73e0b408c89df3c1a12c3b0c45a6fee71bc1de5b47a88fae1a5e69ba6e28', 'salt': '1103733363818826232'}, # sha256('this_can_help_to_confuse_the_attacker_hello1103733363818826232')
    }

    user_data = users_with_pepper_and_salt.get(username)

    if not user_data:
        return False

    # Hash the pepper-prefixed and salted password
    hashed_password = sha256(pepper_prefix + password + user_data['salt'])

    # Check if the password matches
    return user_data['passwordHash'] == hashed_password

# # ----- Test authenticate_with_pepper_and_salt function :
# print(authenticate_with_pepper_and_salt('admin', 'admin') == True)
# print(authenticate_with_pepper_and_salt('admin', 'admin2') == False)
# print(authenticate_with_pepper_and_salt('user', 'hello') == True)
# print(authenticate_with_pepper_and_salt('user', 'helo') == False)
