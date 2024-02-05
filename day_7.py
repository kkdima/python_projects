import random
from day_7_hangman_words import word_list
from day_7_hangman_art import logo, stages

end_of_game = False
lives = 6

print(logo)
# choose random word from list
chosen_word = random.choice(word_list)

print(f'Random word: {chosen_word}')

word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += '_'
    
while not end_of_game:
    guess = input('Guess a guess: ').lower()
    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game = True
        print('You lose.')
        print(f"{' '.join(display)}")
        print(stages[lives])
    if '_' not in display:
        end_of_game = True
        print('You won!')
    print(stages[lives])
    print(f"{' '.join(display)}")