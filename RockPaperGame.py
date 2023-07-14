import random

choices = ['rock', 'paper', 'scissors']
computer_points = 0
player_points = 0

print('-' * 15, 'Play Rock, Paper, and Scissors 10 Rounds with a Computer!', '-' * 15, '\n')

rounds = int(input('Choose Number of rounds!: '))
count = 0
while count < rounds:
    player = input('Rock, Paper, Scissors: ').lower()
    if player not in choices:
        print('Invalid choice! Please choose from rock, paper, or scissors.')
        continue

    computer = random.choice(choices)
    print('Computer: ' + computer)

    if player == computer:
        print('Tie!')
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        print('You Win!')
        player_points += 1
    else:
        print('You Lose!')
        computer_points += 1

    count += 1

print('\n')
print('Your Points: ' + str(player_points))
print('Computer Points: ' + str(computer_points))
print('\n')

if computer_points == player_points:
    print('Overall Tie!')
elif computer_points > player_points:
    print('Overall Computer Won!')
else:
    print('Overall You Won!')
