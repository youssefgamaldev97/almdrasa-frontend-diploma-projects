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

while True:
    computer_input = random.choice(computer_choices)
    print('The computer has made its choice!')

    user_input = ''
    while True:
        user_input = input('Now, it\'s your turn! Please choose your weapon: ')
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
    \rYou chose: {user_input}\n''')

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

    user_restarts = ''
    while True:
        user_restart_list = [['yes', 'y'], ['no', 'n']]
        user_restarts = input('\nDo you want to play again? (Yes/No): ')

        if user_restarts in user_restart_list[0]:
            user_restarts = 'yes'
            break
        elif user_restarts in user_restart_list[1]:
            user_restarts = 'no'
            break
        else:
            print('Enter a valid yes(y)/no(n)')
    
    if user_restarts == 'yes':
        print('')
        continue
    else:
        print(f'''\nThank you for playing! Here\'s how the game went:
        \rYou won: {wins}
        \rThe computer won: {losses}
        \rDraws: {draws}
        \r\nIt\'s been a fun game!''')
        print('\nThanks so much for your time! I hope you had fun playing. Looking forward to seeing you again soon. Goodbye and take care! 👋😊')
        break
