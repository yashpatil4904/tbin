import socket
import random

# Fast modular exponentiation
def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

HOST = "127.0.0.1"
PORT = 5000

def main():
    print("=== DIFFIE-HELLMAN CLIENT ===")

    s = socket.socket()
    s.connect((HOST, PORT))

    # Step 1: Receive p, g, A from server
    data = s.recv(1024).decode()
    p, g, A = map(int, data.split(","))
    print("\n[CLIENT] Received p =", p)
    print("[CLIENT] Received g =", g)
    print("[CLIENT] Received server public key A =", A)

    # Step 2: Choose private key b
    b = random.randint(2, 10)
    print("[CLIENT] Private key b =", b)

    # Step 3: Compute B = g^b mod p
    B = power(g, b, p)
    print("[CLIENT] Public key B = g^b mod p =", B)

    # Step 4: Send B to server
    s.send(str(B).encode())

    # Step 5: Compute shared secret key
    shared_key = power(A, b, p)
    print("[CLIENT] Shared secret key K = A^b mod p =", shared_key)

    print("\n[CLIENT] Key exchange completed.")

    s.close()

if __name__ == "__main__":
    main()
