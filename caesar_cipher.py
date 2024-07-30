from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
position = 0
choice = "yes"

def caesar(text, shift, direction):
    newText = ""
    shift = shift%26

    for i in range(0,len(text)):
        if direction=="encode":
            if text[i] not in alphabet:
                newText += text[i]
            else:
                position = alphabet.index(text[i])
                newText += alphabet[position + shift]
        elif direction=="decode":
            if text[i] not in alphabet:
                newText += text[i]
            else:
                position = alphabet.index(text[i])
                newText += alphabet[position - shift]
        else:
            print("You have entered an invalid option!")

    print(newText)

while choice=="yes":
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    choice = input("Type 'yes' if you want to go again. Otherwise, type 'no'")



