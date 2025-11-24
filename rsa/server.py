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

def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p*q
    phi = (p-1)*(q-1)

    e = 3
    while gcd(e, phi) != 1:
        e += 2

    d = modinv(e, phi)
    return (e, n), (d, n)

# ---------------- SERVER ---------------- #
HOST = "127.0.0.1"
PORT = 5000

def main():
    print("Generating RSA keys for SERVER...")
    public, private = generate_keys()
    e, n = public
    d, _ = private

    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Server running on {HOST}:{PORT}")

    conn, addr = s.accept()
    print("Client connected:", addr)

    # send public key to client
    conn.send(f"{e},{n}".encode())

    # receive encrypted integer
    encrypted = conn.recv(4096).decode().strip()
    encrypted_int = int(encrypted)

    print("\nEncrypted received:", encrypted_int)

    # decrypt
    decrypted_int = pow(encrypted_int, d, n)
    msg = decrypted_int.to_bytes((decrypted_int.bit_length()+7)//8, 'big').decode()

    print("Decrypted message:", msg)

    # reply back
    reply = "OK"
    reply_int = int.from_bytes(reply.encode(), "big")
    encrypted_reply = pow(reply_int, e, n)

    conn.send(str(encrypted_reply).encode())

    conn.close()
    s.close()

if __name__ == "__main__":
    main()
