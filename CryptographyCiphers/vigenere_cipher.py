def vigenere_encrypt(plaintext, key):
    key = key.upper()
    result = []
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            key_index = (key_index + 1) % len(key)

            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(encrypted_char)
        else:
            result.append(char)

    return ''.join(result)


def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    result = []
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            key_index = (key_index + 1) % len(key)

            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            result.append(decrypted_char)
        else:
            result.append(char)

    return ''.join(result)
