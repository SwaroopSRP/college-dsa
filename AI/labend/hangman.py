import random

words = ["apple", "tiger", "chair", "plant"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Enter letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" not in guessed:
    print("You win! Word was:", word)
else:
    print("You lose! Word was:", word)

"""
1. setup → word, guessed list, attempts
2. loop → while attempts & blanks exist
3. check → if guess in word → update positions
4. end → win / lose
"""
