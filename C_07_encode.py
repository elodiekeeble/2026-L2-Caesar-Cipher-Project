alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

message = input("What is your message? ").lower()
shift_number = int(input("How many letters would you like to shift your message by? "))
for letter in message:
    if letter in alphabet:
        new_position = alphabet.index(letter) + shift_number
        print(f"{alphabet[new_position]}")
