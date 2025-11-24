def encrypt(text,key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = key.upper()
    
    result=""
    for ch in text.upper() :
        if ch in alphabet :
            index = alphabet.index(ch)
            result += cipher[index]
        else :
            result+=ch
    return result

def decrypt(ct,key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = key.upper()
    result=""
    for ch in ct.upper():
        if ch in cipher :
            index = cipher.index(ch)
            result += alphabet[index]
        else :
            result += ch
    return result

    
def main():
    key="QWERTYUIOPASDFGHJKLZXCVBNM"
    print("1.encrypt\n 2.decrypt\n 3.exit\n")
    while True :
        choice = int(input("Enter choice"))

        if choice == 1 :
            text = input("Enter plain text :")
            print("Ciphertext : ",encrypt(text,key))
        elif choice == 2: 
            ct = input("Enter cipher text")
            print("Plaintext : ",decrypt(ct,key))
        elif choice ==3 :
            break
        else:
            print("invalid choice")
            
if __name__ == "__main__":
    main()
        
        
        
        