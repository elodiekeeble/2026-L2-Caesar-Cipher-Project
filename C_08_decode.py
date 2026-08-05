import string
alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)

message = input("What is your message? ")
shift_number = int(input("What was your message previously shifted by? "))
decoded_message = ""
for letter in message:
    if letter in alphabet:
        new_position = alphabet.index(letter) - shift_number
        new_position = new_position % len(alphabet)
        decoded_message = decoded_message + alphabet[new_position]
    elif letter in upper_alphabet:
        new_position = upper_alphabet.index(letter) - shift_number
        new_position = new_position % len(upper_alphabet)
        decoded_message = decoded_message + upper_alphabet[new_position]
    else:
        decoded_message = decoded_message + letter

print("This is your decoded message:", decoded_message)
