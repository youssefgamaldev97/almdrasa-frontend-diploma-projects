import random

print('\nWelcome to the classic game of Rock, Paper, Scissors! ✨ Get ready to play against the computer and see who comes out on top. Let\'s have some fun!\n')
print('''Here\'s how the game works:
To choose Rock, type "rock" or "r" or "1".
To choose Paper, type "paper" or "p" or "2".
To choose Scissors, type "scissor" or "s" or "3".
Once you make your choice, the computer will randomly choose one as well, and we\'ll see who wins!\n''')

wins = 0
losses = 0
draws = 0

user_choices = [['rock', 'r', '1'], ['paper', 'p', '2'], ['scissor', 's', '3']]
computer_choices = ['rock', 'paper', 'scissor']

computer_input = random.choice(computer_choices)
print('The computer has made its choice!')

user_input = ''
while True:
    user_input = input('Now, it\'s your turn! Please choose your weapon: ')
    if user_input in user_choices[0] or user_choices[1] or user_choices[2]:
        if user_input in user_choices[0]:
            user_input = 'rock'
            break
        elif user_input in user_choices[1]:
            user_input = 'paper'
            break
        elif user_input in user_choices[2]:
            user_input = 'scissor'
            break
        else:
            print('\nYour input doesn\'t match any of the valid options. Please try again!\n')

print(f'''\nThe computer chose: {computer_input}
You chose: {user_input}\n''')

if (
      user_input == 'rock' and computer_input == 'scissor' or
      user_input == 'paper' and computer_input == 'rock' or
      user_input == 'scissor' and computer_input == 'paper'
   ):
    print('Congratulations! 🎉 You won this round! Rock beats Scissors, Paper beats Rock, and Scissors beats Paper!')
    wins += 1
elif (
        user_input == 'rock' and computer_input == 'rock' or
        user_input == 'paper' and computer_input == 'paper' or
        user_input == 'scissor' and computer_input == 'scissor'
     ):
    print('It\'s a tie! 🤝 Both you and the computer chose the same. Let\'s see what happens next!')
    draws += 1
else:
    print('Oh no! 😢 The computer won this round. Better luck next time!')
    losses += 1

print(f'''\nHere\'s the result of the round:
You won: {wins}
The computer won: {losses}
Draws: {draws}''')
