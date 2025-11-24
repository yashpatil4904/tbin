def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0   # gcd, x, y

    gcd, x1, y1 = extended_euclid(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, y = extended_euclid(a, m)
    if gcd != 1:
        return None     # inverse doesn't exist
    return x % m        # make positive


def menu():
    while True:
        print("\n===== MENU =====")
        print("1. GCD using Extended Euclidean Algorithm")
        print("2. Modular Inverse (a^-1 mod m)")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            gcd, x, y = extended_euclid(a, b)
            print(f"GCD({a}, {b}) = {gcd}")
            print(f"Coefficients: x = {x}, y = {y}")
            print(f"{a}*({x}) + {b}*({y}) = {gcd}")

        elif choice == 2:
            a = int(input("Enter a: "))
            m = int(input("Enter modulus m: "))
            inv = mod_inverse(a, m)
            if inv is None:
                print("Modular inverse does NOT exist (gcd ≠ 1).")
            else:
                print(f"Modular inverse of {a} mod {m} = {inv}")

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")


# Run the menu
menu()
