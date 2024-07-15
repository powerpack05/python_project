import random
import time


def main():

    global count, display, word, already_guessed, play_game

    words_to_guess = [
        "tension",
        "depression",
        "nosleep",
        "unable",
        "mythoughts",
        "continue",
        "break",
    ]

    word = random.choice(words_to_guess)

    length = len(word)

    count = 0

    display = "_" * length

    already_guessed = []

    play_game = ""


def play_loop():

    global play_game
    play_game = input("Do you want to play again? (y/n): ").lower()

    while play_game not in ["y", "n"]:

        play_game = input("Invalid input. Do you want to play again? (y/n): ").lower()

    if play_game == "y":

        main()

    elif play_game == "n":
        print("Thanks for playing! See you next time.")
        exit()


def hangman():
    global count, display, word, already_guessed, play_game
    limit = 5
    while count < limit:
        guess = input(
            f"This is the Hangman Word: {display}\nEnter your guess: "
        ).lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in already_guessed:
                print("You've already guessed that letter. Try again.\n")
                continue
            already_guessed.append(guess)
            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        display = display[:i] + guess + display[i + 1 :]
                print("Correct!\n")
                print(display + "\n")
                if display == word:
                    print("Congratulations! You've guessed the word correctly.")
                    play_loop()
            else:
                count += 1
                if count == limit:
                    print("Wrong guess. You are hanged!\n")
                    print("The word was:", word)
                    play_loop()
                else:
                    print("Wrong guess. Try again.\n")
                    print(f"{limit - count} guesses remaining.\n")
        else:
            print("Invalid input. Please enter a single letter.\n")


# Starting the game
print("\nWelcome to the Hangman Game\n")
name = input("Enter your name: ")
print(f"Hello {name}! Best of luck!")
time.sleep(1)
print("The game is about to begin!\nLet's play Hangman!")
time.sleep(2)

# Initialize the game
main()
hangman()
