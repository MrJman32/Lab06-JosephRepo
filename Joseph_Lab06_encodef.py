def encoder(string):
    encoded_string = []  # empty list

    for ii in string:
        encoded_char = str((int(ii) + 3) % 10)  # 
        encoded_string += encoded_char
        encoded_string = ''.join(encoded_string)

    return encoded_string


#Isabella Camacho Decoder
def decoder(encoded_string):
    decoded_string = []
    for ii in encoded_string:
        for i in range(len(encoded_string)):
            current = int(encoded_string)
            new = str(current - 3)
            decoded_string.append(new)
    return "".join(decoded_string)

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu = int(input("Please enter an option: "))

        if menu == 1:
            string = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            encoded_string = encoder(string)
        if menu == 2:  #Isabella added menu 2
            # updated menu option
            decoded_string = decoder(encoded_string)
            print(f"The encoded password is {encoded_string}, and the original is {string}\n")
        if menu == 3:
            break



if __name__ == '__main__':
    main()