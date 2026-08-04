alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']

message = input("What is your message? ")
shift_number = int(input("How many letters would you like to shift your message by? "))
encoded_message = ""
for letter in message:
    if letter in alphabet:
        new_position = alphabet.index(letter) + shift_number
        new_position = new_position % len(alphabet)
        encoded_message = encoded_message + alphabet[new_position]
    elif letter in upper_alphabet:
        new_position = upper_alphabet.index(letter) + shift_number
        new_position = new_position % len(upper_alphabet)
        encoded_message = encoded_message + upper_alphabet[new_position]
    else:
        encoded_message = encoded_message + letter

print("This is your encoded message: ", encoded_message)
