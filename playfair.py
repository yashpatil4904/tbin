def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            used.add(ch)
            matrix.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J removed
        if ch not in used:
            matrix.append(ch)

    # Convert to 5×5 matrix
    return [matrix[i*5:(i+1)*5] for i in range(5)]


def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])

    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2

    if len(result) % 2 == 1:
        result += 'X'

    return result


def encrypt_playfair(text, matrix):
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # Same row
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:  # Same column
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]
        else:  # Rectangle
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


def decrypt_playfair(text, matrix):
    text = text.upper().replace(" ", "")
    plain = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # Same row
            plain += matrix[r1][(c1 - 1) % 5]
            plain += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:  # Same column
            plain += matrix[(r1 - 1) % 5][c1]
            plain += matrix[(r2 - 1) % 5][c2]
        else:  # Rectangle
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain


def main():
    key = input("Enter Playfair key: ")
    matrix = generate_key_matrix(key)

    print("\nKey Matrix:")
    for row in matrix:
        print(" ".join(row))

    while True:
        print("\n===== PLAYFAIR CIPHER =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            text = input("Enter plaintext: ")
            print("Encrypted:", encrypt_playfair(text, matrix))

        elif choice == '2':
            text = input("Enter ciphertext: ")
            print("Decrypted:", decrypt_playfair(text, matrix))

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
