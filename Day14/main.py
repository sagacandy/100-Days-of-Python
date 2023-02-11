import random


def computer_choice():
    choices = ['rock', 'paper', 'scissor']
    return random.choice(choices)


def determine_winner(player, computer):
    if player == computer:
        return ("Tie"),
    elif player == 'rock':
        if computer == 'paper':
            return ("Computer wins")
        else:
            return ('Player wins')
    elif player == 'paper':
        if computer == 'scissor':
            return ("Computer wins")
        else:
            return ("Player wins")
    elif player == 'scissor':
        if computer == 'rock':
            return ('Computer wins')
        else:
            return ('Player wins')


playerA = input("Choose Rock, Paper, Scissor :").lower()
print(f'You choose {playerA}')
compute = computer_choice()
print(f'Computer choose {compute}')
winner = determine_winner(playerA, compute)
print(f'{winner}')
