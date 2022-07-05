import random 

print("Welcome to Rock, Paper, Scissors Game.")



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
gesturers = [rock, paper, scissors]
user = int(input("Choose 0 for rock, 1 for paper, 2 for scissors:\n"))
if user >2 or user< 0:
    print("You chose a invalid number.")
    print("You lose.")
else:   
    print(gesturers[user])

    computer = random.randint(0,2)
    print("Computer Chose: ")
    print(gesturers[computer])


    if computer == user :
        print("Draw")

    elif gesturers[user] == rock and gesturers[computer] == paper:
        print("You lose")
    elif gesturers[user] == rock and gesturers[computer] == scissors:
        print("You Win")
    elif gesturers[user] == paper and gesturers[computer] == rock:
        print("You Win")
    elif gesturers[user] == paper and gesturers[computer] == scissors:
        print("You lose")
    elif gesturers[user] == scissors and gesturers[computer] == paper:
        print("You Win")
    elif gesturers[user] == scissors and gesturers[computer] == rock:
        print("You lose")
