import random

number_to_guess = random.randint(1,100)


while True:
    try:
        number_guessed = int(input("Guess the number: "))
        if number_guessed == number_to_guess:
            print("Congratulations! You guessed the number.")
            break
        elif number_guessed > number_to_guess:
            print("it's too high")
        elif number_guessed < number_to_guess:
            print("Too low")
    except ValueError:
        print("input a valid whole number between 1 and 100.")

