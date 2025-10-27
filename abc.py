import random
import time
import os

# List of words to use
words = ["apple", "banana", "cherry", "grape", "orange", "mango", "peach", "melon", "berry", "kiwi"]

print("🧠 Welcome to the Memory Quiz Game!")
print("You’ll see some words for a few seconds. Try to remember them!\n")

score = 0

# Main game loop
for round_num in range(3):  # 3 rounds
    print(f"Round {round_num + 1}")
    # Pick random words
    round_words = random.sample(words, 3)
    print("Memorize these words:")
    print(round_words)

    # Wait 5 seconds
    time.sleep(5)

    # Clear screen (works on Windows, Mac, Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Ask user to recall
    answer = input("Enter the words you remember (separate with spaces): ").split()

    # Check matches
    correct = 0
    for word in answer:
        if word in round_words:
            correct += 1

    print(f"You got {correct} out of 3 correct!\n")
    score += correct

print(f"🎉 Final Score: {score} / 9")
print("Thanks for playing!")
