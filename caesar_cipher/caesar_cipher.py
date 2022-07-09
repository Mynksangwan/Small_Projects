from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(text, shift,direction):
    lst = list(text)
    for i in range(len(lst)) : 
        if lst[i] in alphabet:
            if direction == 'encode':
                lst[i] = alphabet[ (alphabet.index(lst[i]) + shift)%26]
            if direction == 'decode':
                lst[i] = alphabet[ (alphabet.index(lst[i]) - shift)%26]
    print(f"Here is your result: {''.join(lst)}\n")

should_continue = True

while should_continue :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    again = input("Type 'yes' if you want to go again otherwise type 'no'.\n").lower().strip()
    if again == 'yes':
        should_continue = True
    else :
        should_continue = False
        print("Goodbye")
