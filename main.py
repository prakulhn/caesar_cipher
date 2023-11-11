alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
    print(f"Here's the encrypted result: {cipher_text}")


def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabets[new_position]
        else:
            plain_text += char
    print(f"Here's the decrypted result: {plain_text}")


exit_program = False
while not exit_program:
    cryption = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Enter the shift number: \n"))
    if cryption == 'encrypt':
        encryption(plain_text=text, shift_key=shift)
    elif cryption == 'decrypt':
        decryption(cipher_text=text, shift_key=shift)
    play_again = input("Enter 'yes' to play again, otherwise enter 'no'. \n")
    if play_again == 'no':
        exit_program = True
        print("Bye, have a good day!!")
