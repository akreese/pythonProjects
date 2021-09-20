#Hangman Game
import random

print("Lets Play hangman")
retry = True
while retry:
    word_list = ["computer", "apple", "korea", "cat", "dog"]
    random_word = str(random.choice(word_list)).lower()
    word_length = len(random_word)
    remaining_lives = word_length + 3
    correct_guesses = 0
    word_alphabet_list = list(random_word)
    print("The word has", word_length, "letters and you have", remaining_lives, "guesses.")
    while remaining_lives > 0:
        print("You have", remaining_lives, "lives left.")
        guess = str(input("Guess an alphabet: "))
        remaining_lives = remaining_lives -1
        if guess in word_alphabet_list:
            correct_guesses = correct_guesses +1
            while guess in word_alphabet_list:
                word_alphabet_list.remove(guess)
            print("Correct guess!", guess, "is in the word!")
            if not word_alphabet_list:
                print("")
                print("YAY! You guess the word ", random_word, " correctly!!")
                break
            elif remaining_lives == 0 and word_alphabet_list:
                print("Maybe next time. The word was:", random_word)
        elif remaining_lives == 0 and word_alphabet_list:
            print("Maybe next time. The word was:", random_word)
    retry_input = str(input("Give it another shot?")).lower()
    if retry_input == "yes":
        retry_input = True
