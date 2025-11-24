def extended_euclid(a, b):
    print("\n=== Extended Euclid Table ===")
    print("a      b      q      r      s1     s2     s      t1     t2     t")
    print("-----------------------------------------------------------------------")

    # Initialize
    a1, b1 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while b1 != 0:
        q = a1 // b1
        r = a1 % b1
        s = s1 - q * s2
        t = t1 - q * t2

        # Print row
        print(f"{a1:<6} {b1:<6} {q:<6} {r:<6} {s1:<6} {s2:<6} {s:<6} {t1:<6} {t2:<6} {t:<6}")

        # Shift values (move row down)
        a1, b1 = b1, r
        s1, s2 = s2, s
        t1, t2 = t2, t

    # Final row (when b1 == 0)
    print(f"{a1:<6} {b1:<6} {'-':<6} {'-':<6} {s1:<6} {s2:<6} {'-':<6} {t1:<6} {t2:<6} {'-':<6}")

    gcd = a1
    x = s1
    y = t1

    print("\nResult:")
    print(f"gcd = {gcd}")
    print(f"x = {x}, y = {y}")
    print(f"{a}*({x}) + {b}*({y}) = {gcd}")

    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, y = extended_euclid(a, m)
    if gcd != 1:
        print("Inverse does not exist.")
        return None
    return x % m


def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Extended Euclid (formatted table)")
        print("2. Modular Inverse")
        print("3. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            extended_euclid(a, b)

        elif ch == 2:
            a = int(input("Enter a: "))
            m = int(input("Enter m: "))
            inv = mod_inverse(a, m)
            if inv is not None:
                print(f"Modular inverse = {inv}")

        elif ch == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

menu()
