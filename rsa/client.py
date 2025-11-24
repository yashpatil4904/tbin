import socket
import random

# ----------- RSA BASIC UTILS ----------- #
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        return None
    return x % m

def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def generate_prime():
    while True:
        p = random.randint(100, 300)
        if is_prime(p):
            return p

# ---------------- CLIENT ---------------- #
HOST = "127.0.0.1"
PORT = 5000

def main():
    s = socket.socket()
    s.connect((HOST, PORT))
    print("Connected to server.")

    # get public key
    e, n = map(int, s.recv(1024).decode().split(","))

    msg = input("Enter a SHORT message: ")

    # convert to int
    msg_int = int.from_bytes(msg.encode(), "big")

    # simple check
    if msg_int >= n:
        print("\nMessage too long! Choose a shorter one.\n")
        s.close()
        return

    encrypted = pow(msg_int, e, n)
    print("\nEncrypted:", encrypted)

    # send encrypted message
    s.send(str(encrypted).encode())

    # receive reply
    reply_enc = int(s.recv(1024).decode())
    reply_dec = pow(reply_enc, 1, n)  # since server used its own e again

    reply = reply_dec.to_bytes((reply_dec.bit_length()+7)//8, 'big').decode()
    print("Server reply:", reply)

    s.close()

if __name__ == "__main__":
    main()
