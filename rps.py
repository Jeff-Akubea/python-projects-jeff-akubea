import random

print("Welcome to Jeff's game of Rock, Paper and scissors")

print("type 'r' for rock, 'p' for paper and 's' for scissors")
print("You can type 'end' to end the game any time")

emojis = {'r': '🪨', 's':'✂️', 'p':'📃'}
sample = ("r","p","s")

your_score = 0
computer_score = 0

while True:
    print()
    computer_choice = random.choice(sample)
    user_input = input("Rock, Paper or scissors (r/p/s): ").lower()

    if user_input == "end":
        print("Thanks for playing.")
        break  
    elif user_input not in sample:
        print("invalid choise")
        continue 

    print(f'You chose {emojis[user_input]}')
    print(f'computer chose {emojis[computer_choice]}')

    if computer_choice == user_input :
        print("It's a tie! Try again.")
    elif (computer_choice == "r" and user_input == "p") or \
        (computer_choice == "p" and user_input =="s") or \
            (computer_choice == "s" and user_input == "r"):
        your_score += 1
        print("you win")
        print("you gained +1")
    elif (computer_choice == "p" and user_input == "r") or\
          (computer_choice == "s" and user_input == "p") or\
                (computer_choice == "r" and user_input == "s"):
        computer_score += 1
        print("you loose")
        print("computer gained +1")
    elif user_input not in sample:
        print("input a valid choise")
print()
print(f'you earned a total of {your_score} points')
print(f'computer earned a total of {computer_score} points')
print()
print("overall winner is:")
if your_score > computer_score:
    print("    You")
elif your_score < computer_score:
    print("     computer")
elif your_score == computer_score:
    print("  It was a tie")

