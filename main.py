# Lucia Weiner encode function
def encode(password):
    encoded_password = ""
    for i in password:
        num = int(i)
        num += 3
        encoded_password += str(num)
    return encoded_password


def main():
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode:")
            print("Your password has been encoded and stored")
            encoded_password = encode(password)

        if choice == 2:
            pass

        if choice == 3:
            break


if __name__ == '__main__':
    main()