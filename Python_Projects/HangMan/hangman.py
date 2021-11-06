import random
import hangman_words
from hangman_art import logo
from hangman_art import stages

display = []
flag = 0
lives = 6
chosen_word = random.choice(hangman_words.word_list)

print(logo)
##print(f'Pssst, the solution is {chosen_word}.')
print("Welcome to hangman, simple game where you should use your brain keeping your luck in hand to guess the word")
print("\n")
print("INSTRUCTION :-\n->Player has 6 lives to guess the word\n->one wrong guess cost one life\n->alert will be displayed on repeating the guessed letter\n->player wins on guessing the word\n->player looses on loosing the life")
print("\n")

for letter in chosen_word:
    display.append('_')

while True:
    guess = input("Guess A Letter : ").lower()
    counter=0
    if guess in display:
        print("You have already guessed "+guess)
    
    for letter in chosen_word:
        if guess == letter:
            display[counter]=letter
            flag = 0
        elif guess not in chosen_word:
            flag = 1
        counter+=1
        
    print(f"{' '.join(display)}")
    if '_' not in display:
        print("You Win")
        break
    
    if flag == 1:
        print("You guessed "+guess+", that's not in the word. You lose a life")
        lives-=1
        print(stages[lives])
        
    if lives == 0:
        print("The Word Is : "+chosen_word)
        print("You Lost")
        break

