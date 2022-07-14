import art 
import random 
from game_data import data 
import os 
clear = lambda: os.system('clear')

def compare(followers_A, followers_B, guess):
    '''Takes user guess and followers counts and return if they got it right'''
    if followers_A > followers_B:
        return guess == 'a'
    else:
        return guess == 'b'

def format_data(random_person):
    '''Takes account data and return formated account data'''
    random_person_name = random_person['name']
    random_person_desc = random_person['description']
    random_person_country = random_person['country']
    return f"{random_person_name}, a {random_person_desc}, from {random_person_country}"

print(art.logo)
score = 0
game_should_continue = True
random_person_B = random.choice(data)

while game_should_continue:

    random_person_A =  random_person_B 
    random_person_B = random.choice(data)
    while random_person_A == random_person_B:
        random_person_B = random.choice(data)

    print(f"Compare A: {format_data(random_person_A)}")
    print(art.vs)
    print(f"Compare B: {format_data(random_person_B)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    followers_A = random_person_A['follower_count']
    followers_B = random_person_B['follower_count']

    is_correct = compare(followers_A, followers_B, guess)

    clear()
    print(art.logo)

    if is_correct:
        score +=1
        print(f"You are right! Current score: {score}")
    else :
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False