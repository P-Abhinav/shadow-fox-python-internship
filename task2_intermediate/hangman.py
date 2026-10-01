"""ShadowFox Python Internship - Task 2: Hangman"""

import random

WORDS = {
    "python": "A popular programming language",
    "github": "A platform for hosting code",
    "computer": "An electronic machine for processing data",
    "database": "Organized collection of data",
    "algorithm": "A step-by-step procedure for solving a problem",
}

HANGMAN_STAGES = [
    "  +---+\n  |   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n=========",
]

MAX_WRONG = len(HANGMAN_STAGES) - 1

def play_game():
    word = random.choice(list(WORDS))
    hint = WORDS[word]
    guessed = set()
    wrong = 0

    print("\n=== HANGMAN ===")
    print("Hint:", hint)

    while wrong < MAX_WRONG:
        display = " ".join(letter if letter in guessed else "_" for letter in word)
        print("\n" + HANGMAN_STAGES[wrong])
        print("Word:", display)
        print("Guessed:", " ".join(sorted(guessed)) or "None")
        print("Attempts remaining:", MAX_WRONG - wrong)

        if all(letter in guessed for letter in word):
            print("You won! 🎉 The word was:", word)
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue
        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)
        if guess not in word:
            wrong += 1
            print("Wrong guess.")
        else:
            print("Good guess!")

    print("\n" + HANGMAN_STAGES[wrong])
    print("You lost. The word was:", word)

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in {"yes", "y"}:
            print("Thanks for playing!")
            break
