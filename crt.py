import math
from typing import List, Tuple

def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean Algorithm: returns (g, x, y) such that ax + by = g = gcd(a,b)."""
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a: int, m: int) -> int:
    """Multiplicative inverse of a modulo m, if it exists."""
    a %= m
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"No inverse: gcd({a}, {m}) = {g}")
    return x % m

def pairwise_coprime(moduli: List[int]) -> bool:
    n = len(moduli)
    for i in range(n):
        if moduli[i] <= 1:
            return False
        for j in range(i+1, n):
            if math.gcd(moduli[i], moduli[j]) != 1:
                return False
    return True

def crt_reconstruct(residues: List[int], moduli: List[int]) -> int:
    """Reconstruct C from residues using CRT formula."""
    if len(residues) != len(moduli):
        raise ValueError("residues and moduli length mismatch")
    M = 1
    for m in moduli:
        M *= m
    total = 0
    for (a_i, m_i) in zip(residues, moduli):
        M_i = M // m_i
        inv = modinv(M_i % m_i, m_i)
        total = (total + (a_i % m_i) * M_i * inv) % M
    return total

def to_residues(x: int, moduli: List[int]) -> list:
    return [x % m for m in moduli]

def compute_op(a_res: list, b_res: list, moduli: list, op: str) -> list:
    c_res = []
    for (ai, bi, mi) in zip(a_res, b_res, moduli):
        if op == '1':  # addition
            ci = (ai + bi) % mi
        elif op == '2':  # subtraction
            ci = (ai - bi) % mi
        elif op == '3':  # multiplication
            ci = (ai * bi) % mi
        elif op == '4':  # division
            if math.gcd(bi, mi) != 1:
                raise ZeroDivisionError(f"Division undefined modulo {mi}: gcd({bi}, {mi}) != 1")
            ci = (ai * modinv(bi, mi)) % mi
        else:
            raise ValueError("Unknown operation")
        c_res.append(ci)
    return c_res

def print_residues(label: str, residues: list, moduli: list):
    pairs = ", ".join([f"{r} (mod {m})" for r, m in zip(residues, moduli)])
    print(f"{label}: [" + pairs + "]")

def main():

    while True:
        try:
            k = int(input("Enter number of congruences (k): ").strip())
            if k <= 0:
                print("k must be positive.")
                continue
            print("Enter", k, "pairwise coprime moduli m_i (space-separated): ", end="")
            moduli = list(map(int, input().strip().split()))
            if len(moduli) != k:
                print("Expected", k, "moduli. Try again.\n")
                continue
            if not pairwise_coprime(moduli):
                print("Moduli must be pairwise coprime and > 1. Try again.\n")
                continue
            break
        except Exception as e:
            print("Error:", e, "\nTry again.\n")

    M = 1
    for m in moduli:
        M *= m
    print(f"\nSystem initialized. M = Π m_i = {M}")
    print("Available operations:")
    print("  1) Addition   (C = A + B mod M)")
    print("  2) Subtraction(C = A - B mod M)")
    print("  3) Multiplication (C = A * B mod M)")
    print("  4) Division   (C = A / B mod M)  [Requires B invertible modulo each m_i]")
    print("  5) Quit")

    while True:
        op = input("\nChoose option [1-5]: ").strip()
        if op == '5':
            print("Quit!")
            break
        if op not in {'1','2','3','4'}:
            print("Invalid choice. Try again.")
            continue
        try:
            A = int(input("Enter large integer A: ").strip())
            B = int(input("Enter large integer B: ").strip())
        except Exception:
            print("Invalid integers. Try again.")
            continue

        a_res = to_residues(A, moduli)
        b_res = to_residues(B, moduli)

        print_residues("A residues", a_res, moduli)
        print_residues("B residues", b_res, moduli)

        try:
            c_res = compute_op(a_res, b_res, moduli, op)
        except ZeroDivisionError as zde:
            print(zde)
            continue

        print_residues("C residues (per modulus)", c_res, moduli)
        C = crt_reconstruct(c_res, moduli)
        print(f"Reconstructed C (0 ≤ C < M): {C}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting...")

