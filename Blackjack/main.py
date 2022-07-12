from art import logo
import os
clear = lambda: os.system('clear')
import random

def blackjack():
    print(logo)

    def deal_card():
        """Returns a random card from deck."""
        cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card 

    def score(arr):
        """Takes a list of cards and returns it's score"""
        if sum(arr) == 21 and len(arr) ==2:
            return 0 

        if 11 in arr and sum(arr)>21:
            arr.remove(11)
            arr.append(1)

        return sum(arr)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card()]

    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {computer_cards}")

    while score(computer_cards)<17 and score(computer_cards) != 0:
        computer_cards.append(deal_card())

    should_add_user = True

    while should_add_user:
        if score(user_cards)<21 and score(user_cards) !=0:
            add_another_card = input("Type 'y' to get another card, type 'n' to pass :")
            if add_another_card == 'y' :
                user_cards.append(deal_card())
                print(f"Your current hand: {user_cards}")
            else:
                should_add_user = False
        else:
            should_add_user = False


    print(f"Your final Hand: {user_cards}")
    print(f"Computer's final hand: {computer_cards}")

    print(compare(score(user_cards), score(computer_cards)))

    play_again = input("Type 'yes' to play again, Type 'no' to quit : ").lower()
    if play_again == 'yes':
        clear()
        blackjack()
    else: 
        clear()

blackjack()