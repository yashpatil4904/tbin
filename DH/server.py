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
    print("=== DIFFIE-HELLMAN SERVER ===")

    # Step 1: Choose prime p and generator g
    p = 23                     # small prime for lab demo
    g = 5                      # primitive root modulo p

    print("\n[SERVER] Prime p =", p)
    print("[SERVER] Generator g =", g)

    # Step 2: Server chooses private key 'a'
    a = random.randint(2, 10)
    print("[SERVER] Private key a =", a)

    # Step 3: Compute public key A = g^a mod p
    A = power(g, a, p)
    print("[SERVER] Public key A = g^a mod p =", A)

    # Create socket
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)

    print("\n[SERVER] Waiting for client connection...")
    conn, addr = s.accept()
    print("[SERVER] Client connected:", addr)

    # Step 4: Send p, g, A to client
    conn.send(f"{p},{g},{A}".encode())

    # Step 5: Receive B from client
    B = int(conn.recv(1024).decode())
    print("[SERVER] Received client public key B =", B)

    # Step 6: Compute shared secret
    shared_key = power(B, a, p)
    print("[SERVER] Shared secret key K = B^a mod p =", shared_key)

    print("\n[SERVER] Key exchange completed.")

    conn.close()
    s.close()

if __name__ == "__main__":
    main()
