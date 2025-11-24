def generate_key(text, key):
    key = key.upper()
    text = text.upper()
    key = list(key)

    if len(key) == len(text):
        return "".join(key)

    # extend key
    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])

    return "".join(key)


def encrypt(text, key):
    text = text.upper()
    key = generate_key(text, key)
    cipher = ""

    for t, k in zip(text, key):
        if t.isalpha():
            c = chr((ord(t) + ord(k) - 2*65) % 26 + 65)
            cipher += c
        else:
            cipher += t
    return cipher


def decrypt(cipher, key):
    cipher = cipher.upper()
    key = generate_key(cipher, key)
    plain = ""

    for c, k in zip(cipher, key):
        if c.isalpha():
            p = chr((ord(c) - ord(k) + 26) % 26 + 65)
            plain += p
        else:
            plain += c
    return plain


def main():
    while True:
        print("\n===== POLYALPHABETIC (VIGENERE) CIPHER =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            text = input("Enter plaintext: ")
            key = input("Enter key: ")
            print("Encrypted Text:", encrypt(text, key))

        elif choice == '2':
            text = input("Enter ciphertext: ")
            key = input("Enter key: ")
            print("Decrypted Text:", decrypt(text, key))

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
