import numpy as np

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_inverse_2x2(mat):
    det = int(np.round(np.linalg.det(mat))) % 26
    inv_det = mod_inverse(det, 26)
    if inv_det is None:
        return None

    # adjoint matrix
    a, b, c, d = mat[0][0], mat[0][1], mat[1][0], mat[1][1]
    adj = np.array([[d, -b], [-c, a]])

    return (inv_det * adj) % 26

def text_to_matrix(text):
    text = text.upper().replace(" ", "")
    if len(text) % 2 == 1:
        text += "X"
    nums = [ord(ch) - 65 for ch in text]
    return np.array(nums).reshape(-1, 2)

def matrix_to_text(mat):
    text = ""
    for r in mat:
        for num in r:
            text += chr((int(num) % 26) + 65)
    return text

def encrypt(plaintext, key):
    mat = text_to_matrix(plaintext)
    cipher = (mat @ key) % 26
    return matrix_to_text(cipher)

def decrypt(ciphertext, key):
    inv_key = matrix_inverse_2x2(key)
    if inv_key is None:
        return "Decryption not possible (key is not invertible mod 26)"
    mat = text_to_matrix(ciphertext)
    plain = (mat @ inv_key) % 26
    return matrix_to_text(plain)

def main():
    print("Enter 2×2 Hill Cipher key matrix:")
    k11 = int(input("k11: "))
    k12 = int(input("k12: "))
    k21 = int(input("k21: "))
    k22 = int(input("k22: "))

    key = np.array([[k11, k12], [k21, k22]]) % 26

    while True:
        print("\n===== HILL CIPHER =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        ch = input("Enter choice: ")

        if ch == '1':
            pt = input("Enter plaintext: ")
            print("Encrypted:", encrypt(pt, key))

        elif ch == '2':
            ct = input("Enter ciphertext: ")
            print("Decrypted:", decrypt(ct, key))

        elif ch == '3':
            print("Exiting...")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()

    """[3 3,
        2 5]"""
