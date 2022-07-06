import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator.\n")
n_letters = int(input("How many letter would you like in your password:\n"))
n_symbols = int(input("How many symbols would you like in your passowrd:\n"))
n_numbers = int(input("How many numbers would you like in your passoword:\n"))

password = ""

for letter in range(n_letters):
    password += letters[random.randint(0,len(letters)-1)]

for number in range(n_numbers):
    password += numbers[random.randint(0,len(numbers)-1)]

for symbol in range(n_symbols):
    password += symbols[random.randint(0, len(symbols)-1)]

ans = ""

for _ in range(len(password)):
    ans += password[random.randint(0, len(password)-1)]

print(f"Your Password: {ans}")