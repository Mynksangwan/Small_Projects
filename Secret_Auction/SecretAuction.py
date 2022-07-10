from art import logo
import os
clear = lambda: os.system('clear')

print(logo)
print("Welcome to secret Auction")
dic = {}

def highest_bidder(bidding_record):
    highest = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest:
            highest = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")

bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("Place your bid : $"))

    dic[name] = bid 

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == 'no':
        bidding_finished = True
        highest_bidder(dic)
    elif should_continue == 'yes':
        clear()
