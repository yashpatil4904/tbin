# ------------------------------------------
# Row Rail Fence (Zig-Zag) Encrypt
# ------------------------------------------
def row_rail_encrypt(text, key):
    rails = ['' for _ in range(key)]
    row, step = 0, 1

    for ch in text:
        rails[row] += ch
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return ''.join(rails)


# ------------------------------------------
# Row Rail Fence (Zig-Zag) Decrypt
# ------------------------------------------
def row_rail_decrypt(cipher, key):
    rail = [['' for _ in range(len(cipher))] for _ in range(key)]

    row, step = 0, 1
    for i in range(len(cipher)):
        rail[row][i] = '*'
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    idx = 0
    for r in range(key):
        for c in range(len(cipher)):
            if rail[r][c] == '*' and idx < len(cipher):
                rail[r][c] = cipher[idx]
                idx += 1

    row, step = 0, 1
    result = ""
    for i in range(len(cipher)):
        result += rail[row][i]
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return result


# ------------------------------------------
# Columnar Transposition Encrypt
# ------------------------------------------
def column_encrypt(text, cols):
    grid = ['' for _ in range(cols)]
    for i, ch in enumerate(text):
        grid[i % cols] += ch
    return ''.join(grid)


# ------------------------------------------
# Columnar Transposition Decrypt
# ------------------------------------------
def column_decrypt(cipher, cols):
    n = len(cipher)
    col_lengths = [n // cols] * cols
    for i in range(n % cols):
        col_lengths[i] += 1

    cols_data = []
    idx = 0
    for length in col_lengths:
        cols_data.append(cipher[idx:idx + length])
        idx += length

    result = ""
    pointers = [0] * cols

    for i in range(n):
        col = i % cols
        if pointers[col] < len(cols_data[col]):
            result += cols_data[col][pointers[col]]
            pointers[col] += 1

    return result


# ------------------------------------------
# Double Row-Column Rail Fence Encrypt
# ------------------------------------------
def double_encrypt(text, rail_key, col_key):
    step1 = row_rail_encrypt(text, rail_key)
    final = column_encrypt(step1, col_key)
    return final


# ------------------------------------------
# Double Row-Column Rail Fence Decrypt
# ------------------------------------------
def double_decrypt(cipher, rail_key, col_key):
    step1 = column_decrypt(cipher, col_key)
    final = row_rail_decrypt(step1, rail_key)
    return final


# ------------------------------------------
# MENU PROGRAM
# ------------------------------------------
def main():
    while True:
        print("\n===== DOUBLE ROW-COLUMN RAIL FENCE =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            text = input("Enter plaintext: ").replace(" ", "")
            rail_key = int(input("Enter rail key: "))
            col_key = int(input("Enter column key: "))

            cipher = double_encrypt(text, rail_key, col_key)
            print("Encrypted:", cipher)

        elif choice == "2":
            cipher = input("Enter ciphertext: ")
            rail_key = int(input("Enter rail key: "))
            col_key = int(input("Enter column key: "))

            plain = double_decrypt(cipher, rail_key, col_key)
            print("Decrypted:", plain)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")    


if __name__ == "__main__":
    main()
