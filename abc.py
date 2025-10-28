import random
import time
import os

# List of words to use in the game
WORDS = [
    "apple", "banana", "cherry", "grape", "orange",
    "mango", "peach", "melon", "berry", "kiwi",
    "papaya", "plum", "pear", "lemon", "coconut"
]

def clear_screen():
    """Clears the terminal screen (Windows/Mac/Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def memory_quiz():
    print("🧠 Welcome to the Memory Quiz Game!")
    print("You’ll see some words for a few seconds — try to remember them!\n")

    score = 0
    total_rounds = 3

    for round_num in range(1, total_rounds + 1):
        print(f"🔹 Round {round_num}")
        # Pick random words
        round_words = random.sample(WORDS, 3)
        print("Memorize these words:")
        print(", ".join(round_words))

        # Wait 5 seconds before clearing
        time.sleep(5)
        clear_screen()

        # Ask user to recall
        answer = input("Enter the words you remember (separate with spaces): ").lower().split()

        # Calculate correct answers
        correct = len(set(answer) & set(round_words))
        print(f"✅ You got {correct} out of 3 correct!\n")

        score += correct
        time.sleep(2)
        clear_screen()

    print(f"🎉 Final Score: {score} / {total_rounds * 3}")
    print("Thanks for playing the Memory Quiz Game!")

if __name__ == "__main__":
    memory_quiz()
