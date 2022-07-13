from art import logo
import random 

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()


if difficulty == 'easy':
    guess = 10
else:
    guess = 5
    

while guess>0:
    print(f"You have {guess} attempts remaining to guess the number.")
    user_number = int(input("Make a guess: "))
    if user_number == random_number:
        print(f"You got it. The answer was {random_number}")
        break
    elif user_number > random_number:
        print("Too high.")  
        guess -=1  
    else:
        print("Too low.")  
        guess -=1
    
    if guess != 0 :
        print("Guess Again.")
    else:
        print("You ran out of guesses. You lose!.")
        print(f"Answer was {random_number}")