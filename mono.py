def encrypt(plaintext, key_map):
    ciphertext = ""
    for ch in plaintext.upper():
        if ch.isalpha():
            ciphertext += key_map[ch]
        else:
            ciphertext += ch
    return ciphertext


def decrypt(ciphertext, key_map):
    reverse_map = {v: k for k, v in key_map.items()}
    plaintext = ""
    for ch in ciphertext.upper():
        if ch.isalpha():
            plaintext += reverse_map[ch]
        else:
            plaintext += ch
    return plaintext


def main():
    # Example fixed key (you can also randomize if needed)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"

    key_map = {plain: cipher for plain, cipher in zip(alphabet, cipher_alphabet)}

    while True:
        print("\n===== MONOALPHABETIC CIPHER =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == '1':
            text = input("Enter plaintext: ")
            print("Encrypted text:", encrypt(text, key_map))

        elif choice == '2':
            text = input("Enter ciphertext: ")
            print("Decrypted text:", decrypt(text, key_map))

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
