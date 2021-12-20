import random

rd = random.randint(1,9)
guess = 0
while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 9")

    if guess == "exit":
        break
    guess = int(guess)

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:

        print("Right!")

