import random 
import hangman_words 
import hangman_art as H

print(H.logo)


word_list = hangman_words.word_list

#choose a random word from list

chosen_word = word_list[random.randint(0,len(word_list)-1)]
#Test code
#print(chosen_word)


#Create a list of dashes of length equal to length of chosen_word

dash = []
for _ in range(len(chosen_word)):
    dash += "_"

# creating a string for better UI
print(f"{' '.join(dash)}\n")


life = 6
blank_filled = True

while life>0 and blank_filled:

    #Asks the user for a guess 
    guess = input("Guess a letter: ").lower() 

    #telling if user already guessed the character
    if guess in dash:
        print(f"You have already guessed {guess}\n")

    #Checking if the guess character is present in chosen_word, 
    # and if it is there, replacing the dashs at those positions with guess character 
    #if not decreasing life and showing hangman art progressing
    for i  in range(len(chosen_word)):
        if chosen_word[i] == guess :
            dash[i] = guess

    #checking if word is completed or not
    blank_filled = "_" in dash


    if guess not in chosen_word: 
        print(f"You chose {guess}, which is not in word. You lose a life.\n")
        life -=1 
        print(H.stages[life])
       
    print(f"{' '.join(dash)}\n")

if life>0 :
    print("YOU WON")
if life == 0 :
     print("YOU LOSE")
     print(f"Word was {chosen_word}")


