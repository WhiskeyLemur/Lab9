def encode(password):
    encoded = ""
    for char in password:
        encoded += str(int(char) + 3)
    return encoded

def decode(password):
    deccoded = ""
    for char in password:
        decoded += str(int(char) - 3)
    return decoded

def main():
    while True:
        print(
'''\nMenu
-------------
1. Encode
2. Decode
3. Quit\n''')
        
        option = int(input("Please enter an option: "))
        match(option):
            case 1:
                pw_raw = input("Please enter the password to encode: ")
                password = encode(pw_raw)
                print("Your password has been encoded and stored!")
            case 2:
                print(f"The encoded password is {password}, and the original password is {pw_raw}")
            case 3:
                exit()

if __name__ == "__main__":
    main()