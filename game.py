import random

def play_pot_thong():
    print("Welcome to Pot Thong!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess the number in the fewest attempts possible.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break

    print("Thanks for playing Pot Thong!") #Выводим результат на экран

play_pot_thong()
