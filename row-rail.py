def encrypt_rail_fence(text, key):
    rails = ['' for _ in range(key)]
    row = 0
    step = 1

    for ch in text:
        rails[row] += ch
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return ''.join(rails)


def decrypt_rail_fence(cipher, key):
    # Build empty rail structure
    rail = [['' for _ in range(len(cipher))] for _ in range(key)]

    # Step positions zig-zag
    row = 0
    step = 1
    for i in range(len(cipher)):
        rail[row][i] = '*'
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    # Fill characters
    idx = 0
    for r in range(key):
        for c in range(len(cipher)):
            if rail[r][c] == '*' and idx < len(cipher):
                rail[r][c] = cipher[idx]
                idx += 1

    # Read message in zig-zag
    row = 0
    step = 1
    result = ""
    for i in range(len(cipher)):
        result += rail[row][i]
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return result


def main():
    while True:
        print("\n===== ROW RAIL FENCE CIPHER =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            text = input("Enter plaintext: ").replace(" ", "")
            key = int(input("Enter key (number of rails): "))
            cipher = encrypt_rail_fence(text, key)
            print("Encrypted Text:", cipher)

        elif choice == "2":
            cipher = input("Enter ciphertext: ")
            key = int(input("Enter key (number of rails): "))
            plaintext = decrypt_rail_fence(cipher, key)
            print("Decrypted Text:", plaintext)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
