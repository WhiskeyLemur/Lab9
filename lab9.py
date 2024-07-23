def encode(password):
    encoded = ""
    for char in password:
        if int(char) >= 7:
            encoded += str(int(char) - 7)
            continue
        encoded += str(int(char) + 3)
        
    return encoded

# DECODE MISSING!!!!!!!!!!!!!

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