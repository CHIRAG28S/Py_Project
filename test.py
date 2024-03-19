import random

from word_file import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_end = False
lives = 6

from art import logo
print(logo)


display = []
for _ in range(word_length):
    display += "_"

while not game_end:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            game_end = True
            print("You lose.")
            print("the correct word was",chosen_word)

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_end = True
        print("You win.")

    from art import stages
    print(stages[lives])