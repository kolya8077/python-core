#камінь - rock, папір - paper, ножиці - scissors

import random

print(" \t\tWelcome to the game")
print("\t\tRock Paper Scissors")

user = 0
bot = 0

user_score = 0
bot_score = 0
while True:
    user_score = 0
    bot_score = 0
    for i in range(3):
        print('-'*20,f'Round [{i+1}]' )
        while True:
            user = input('\t[r] - rock;\n\t[p] - paper;\n\t[s] - scissors;\n\tEnter your choice: ')
            user = user.lower()
            # if user == ['r', 'p', 's']:
            if user == 'r' or user == 'p' or user == 's':
                break
            else:
                print('Try again enter new symbol ')

        bot = random.choice('rps')
        print('\tBot\tUser')
        print(f'\t {bot}\t{user}')
        if user == 'r' and bot == 's' or user == 'p' and bot == 'r' or user == 's' or bot == 'p':
            user_score += 1
        elif bot == 'r' and user == 'r' or bot == 'p' and user == 'r' or bot == 's' or user == 'p':
            bot_score += 1

    if user_score > bot_score:
        print('============================You are winner============================')
    elif bot_score > user_score:
        print('============================Bot is winner============================')
    else:
        print('============================Draw============================')
    
    while True:
        user_choise = input('Play again? [y] - YES; [n] - NO : ')
        user_choise = user_choise.lower()
        if user_choise == 'y' or user_choise == 'n':
            break
        else:
            print('Enter your choice !!!')
    if user_choise == 'n':
        break