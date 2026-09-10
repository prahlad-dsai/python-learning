import random

secret_number = random.randint(1, 100)
difficulty = input("Please state your level :(easy, meduim, hard)").strip().lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "medium":
    attempts = 7
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid difficulty")
    exit()

for attempt in range(attempts):
    guess = int(input("Guess a number from 1 to 100: "))

    if guess == secret_number:
        print("Correct! You won.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print("You're out of guesses. The number was: ", secret_number)


