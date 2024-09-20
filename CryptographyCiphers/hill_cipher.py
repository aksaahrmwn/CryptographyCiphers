# hill_cipher.py

import numpy as np

def create_matrix_key(key):
    key = key.replace(" ", "")
    size = int(len(key) ** 0.5)
    key_matrix = [[ord(char) - 65 for char in key[i:i+size]] for i in range(0, len(key), size)]
    return np.array(key_matrix)

def text_to_vector(text):
    return [ord(char.upper()) - 65 for char in text]

def vector_to_text(vector):
    return ''.join(chr(num + 65) for num in vector)

def hill_encrypt(plaintext, key):
    n = len(key)
    matrix_key = create_matrix_key(key)
    plaintext_vector = text_to_vector(plaintext)

    # Ensure length of plaintext is a multiple of matrix size
    if len(plaintext_vector) % n != 0:
        padding_length = n - len(plaintext_vector) % n
        plaintext_vector += [ord('X') - 65] * padding_length  # Padding with 'X'

    ciphertext = ""
    for i in range(0, len(plaintext_vector), n):
        vector_chunk = np.array(plaintext_vector[i:i+n])
        encrypted_vector = np.dot(matrix_key, vector_chunk) % 26
        ciphertext += vector_to_text(encrypted_vector)

    return ciphertext

def hill_decrypt(ciphertext, key):
    n = len(key)
    matrix_key = create_matrix_key(key)
    matrix_key_inv = np.linalg.inv(matrix_key)  # Find inverse of key matrix
    matrix_key_inv = np.round(matrix_key_inv).astype(int) % 26  # Modulo 26 and round

    ciphertext_vector = text_to_vector(ciphertext)
    plaintext = ""

    for i in range(0, len(ciphertext_vector), n):
        vector_chunk = np.array(ciphertext_vector[i:i+n])
        decrypted_vector = np.dot(matrix_key_inv, vector_chunk) % 26
        plaintext += vector_to_text(np.round(decrypted_vector).astype(int))

    return plaintext

# Example usage
if __name__ == "__main__":
    key = "GYBNQKURP"  # This is a 3x3 matrix
    plaintext = "ACT"
    encrypted = hill_encrypt(plaintext, key)
    decrypted = hill_decrypt(encrypted, key)

    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
