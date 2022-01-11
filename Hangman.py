import random
from art import stages, logo
from words import word_list

print(logo)
lives = 6
game_is_finished = False
chosen_word = random.choice(word_list)
display = []
for l in chosen_word:
    display += "_"
print(f"\n{' '.join(display)}")
while not game_is_finished:
    guess = input("\nGuess a letter : ")
    user_guess = guess.lower()
    if user_guess in display:
        print(f"\nYou've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    if user_guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("\n\nYOU LOSE.")
  
    if not "_" in display:
        game_is_finished = True
        print("\n\nYOU WIN.")
        
    print(stages[lives])
print(f"\nWord was : {chosen_word}\n")

