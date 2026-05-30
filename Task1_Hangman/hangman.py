import random

words = ["python", "hangman", "coding", "laptop", "bridge"]
word = random.choice(words)
guessed = []
wrong = 0

print("Welcome to Hangman!")
print("Guess the word letter by letter. You have 6 attempts.\n")

while wrong < 6:
    display = [l if l in guessed else "_" for l in word]
    print("Word: " + " ".join(display))
    print(f"Wrong guesses: {wrong}/6")
    
    if "_" not in display:
        print("\nCongratulations! You guessed the word:", word)
        break
    
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue
    
    if guess in guessed:
        print("You already guessed that letter.\n")
        continue
    
    if guess in word:
        guessed.append(guess)
        print("Correct!\n")
    else:
        guessed.append(guess)
        wrong += 1
        print(f"Wrong! {6 - wrong} attempts left.\n")
else:
    print(f"\nGame Over! The word was: {word}")