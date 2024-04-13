import random

VALID_OPTIONS = ['rock', 'paper', 'scissors']

def get_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or 
        (player == 'scissors' and computer == 'paper')):
        prompt('You win!')
    elif (player == computer):
        prompt("It's a tie!")
    else:
        prompt('You lose!')
    prompt(f"You picked: {player}. Computer picked: {computer}")

def prompt(message):
    print(f'==> {message}')

while True:

    prompt(f"Enter {', '.join(VALID_OPTIONS)}")
    choice = input()

    while choice not in VALID_OPTIONS:
        prompt(f"Oops! That's not a valid option!")
        prompt(f"Please enter {', '.join(VALID_OPTIONS)}")
        choice = input()

    computer_choice = random.choice(VALID_OPTIONS)

    get_winner(choice, computer_choice)

    prompt("Do you want to play again? (y/n)")
    play_again = input().lower()

    while True:
        if play_again.startswith('n') or play_again.startswith('y'):
            break
        
        prompt("Please enter 'y' or 'n'")
        play_again = input().lower()

    if play_again[0] == 'n':
        break
