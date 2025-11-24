def extended_euclid(a, b):
    # Initialize remainders
    r1, r2 = a, b

    # Initialize coefficients for Bézout identity
    t1, t2 = 1, 0     # corresponds to r1
    s1, s2 = 0, 1     # corresponds to r2

    print("\n=== Extended Euclidean Algorithm ===")
    print("a   b   q    t1   t2   s1   s2")
    print("------------------------------------")

    while r2 != 0:
        q = r1 // r2    # quotient

        print(f"{r1:<4} {r2:<4} {q:<4}  {t1:<4} {t2:<4} {s1:<4} {s2:<4}")

        # Update remainders
        r = r1 - q * r2
        r1, r2 = r2, r

        # Update t values
        t = t1 - q * t2
        t1, t2 = t2, t

        # Update s values
        s = s1 - q * s2
        s1, s2 = s2, s

    print(f"{r1:<4} {r2:<4} {'-':<4}  {t1:<4} {t2:<4} {s1:<4} {s2:<4}")
    print("------------------------------------")

    # r1 is gcd, coefficients are t1 and s1
    return r1, t1, s1


def mod_inverse(a, m):
    gcd, x, y = extended_euclid(a, m)
    if gcd != 1:
        return None
    return x % m


def menu():
    while True:
        print("\n===== MENU =====")
        print("1. GCD using Extended Euclid (with t, t1, t2)")
        print("2. Modular Inverse")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            gcd, x, y = extended_euclid(a, b)
            print(f"\nGCD({a}, {b}) = {gcd}")
            print(f"Coefficients: x = {x}, y = {y}")
            print(f"{a}*({x}) + {b}*({y}) = {gcd}")

        elif choice == 2:
            a = int(input("Enter a: "))
            m = int(input("Enter modulus m: "))
            inv = mod_inverse(a, m)
            if inv is None:
                print("Inverse does NOT exist (gcd ≠ 1).")
            else:
                print(f"Modular inverse of {a} mod {m} = {inv}")

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


menu()
