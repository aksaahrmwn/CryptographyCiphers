# playfair_cipher.py

def generate_playfair_matrix(key):
    matrix = []
    key = key.upper().replace("J", "I")  # Replace J with I as per Playfair rules
    used_letters = set()

    # Add unique letters of the key to the matrix
    for letter in key:
        if letter not in used_letters and letter.isalpha():
            matrix.append(letter)
            used_letters.add(letter)

    # Add remaining letters of the alphabet
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        if letter not in used_letters:
            matrix.append(letter)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]  # 5x5 matrix

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def playfair_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    matrix = generate_playfair_matrix(key)
    digraphs = []

    # Prepare digraphs
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i + 1]
        else:
            b = 'X'  # Pad with X if odd length
        if a == b:
            digraphs.append((a, 'X'))
            i += 1
        else:
            digraphs.append((a, b))
            i += 2

    ciphertext = []
    for a, b in digraphs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row
            ciphertext.append(matrix[row1][(col1 + 1) % 5])
            ciphertext.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column
            ciphertext.append(matrix[(row1 + 1) % 5][col1])
            ciphertext.append(matrix[(row2 + 1) % 5][col2])
        else:  # Rectangle rule
            ciphertext.append(matrix[row1][col2])
            ciphertext.append(matrix[row2][col1])

    return ''.join(ciphertext)

def playfair_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace("J", "I").replace(" ", "")
    matrix = generate_playfair_matrix(key)
    digraphs = [(ciphertext[i], ciphertext[i + 1]) for i in range(0, len(ciphertext), 2)]

    plaintext = []
    for a, b in digraphs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row
            plaintext.append(matrix[row1][(col1 - 1) % 5])
            plaintext.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            plaintext.append(matrix[(row1 - 1) % 5][col1])
            plaintext.append(matrix[(row2 - 1) % 5][col2])
        else:  # Rectangle rule
            plaintext.append(matrix[row1][col2])
            plaintext.append(matrix[row2][col1])

    return ''.join(plaintext)

# Example usage
if __name__ == "__main__":
    key = "KEYWORD"
    plaintext = "HELLOWORLD"
    encrypted = playfair_encrypt(plaintext, key)
    decrypted = playfair_decrypt(encrypted, key)

    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
