# Semyon Baykov
# Encoder stores the encoded password to a new variable, with each digit being shifted up by 3 numbers
def encode(pswd):
    output = ''
    for i in range(len(pswd)):
        output += str(int(pswd[i]) + 3)[-1]
    return output


# Decoder code goes here (inverse of encode())
def decode(pswd):
    pass


# Main function with menu loop
def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        opt = input('Please enter an option: ')
        if opt == '1':
            pswd = encode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!\n')
        elif opt == '2':
            print(f'The encoded password is {pswd}, and the original password is {decode(pswd)}.\n')
        else:
            return


# Call main
if __name__ == '__main__':
    main()