def encoder(string):
    encoded_string = []  # empty list

    for ii in string:
        encoded_char = str((int(ii) + 3) % 10)  # 
        encoded_string += encoded_char
        encoded_string = ''.join(encoded_string)

    return encoded_string


def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu = int(input("Please enter an option: "))

        if menu == 1:
            string = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")

        if menu == 2:
            pass

        if menu == 3:
            break


if __name__ == '__main__':
    main()