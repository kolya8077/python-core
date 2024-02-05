#камінь - rock, папір - paper, ножиці - scissors

import random

print("\t\tWelcome to the game")
print("\t\tRock Paper Scissors")


user_statistic = 0
bot_statistic = 0
draw_statistic = 0

while True:
    user_score = 0
    bot_score = 0
    
    for i in range(5):
        print('-'*20,f'Round [{i+1}]' )
        while True:
            user = input('\t[r] - rock;\n\t[p] - paper;\n\t[s] - scissors;\n\t[v] - spock;\n\t[l] - lizard;\n\tEnter your choice: ')
            user = user.lower()
            # if user == ['r', 'p', 's']:
            if user in ['r', 'p', 's', 'v', 'l']:
                break
            else:
                print('Try again enter new symbol ')

        bot = random.choice('rpsvl')
        print('\tBot\tUser')
        print(f'\t {bot}\t{user}')
        
        win_keys = {'r': {'s', 'l'}, 'l': {'v', 'p'}, 'v': {'r', 's'}, 's': {'l', 'p'}, 'p': {'v', 'r'}}

        if bot in win_keys[user]:
            user_score += 1
        elif user in win_keys[bot]:
            bot_score += 1

    if user_score > bot_score:
        user_statistic += 1
        print('============================You are winner============================')
    elif bot_score > user_score:
        bot_statistic += 1
        print('============================Bot is winner============================')
    else:
        draw_statistic += 1
        print('============================Draw============================')
    
    while True:
        user_choise = input('Play again? [y] - YES; [n] - NO : ')
        user_choise = user_choise.lower()
        if user_choise == 'y' or user_choise == 'n':
            break
        else:
            print('Enter your choice !!!')
            
    if user_choise == 'n':
        print(f'''
            Bot win :: {bot_statistic}
            User win :: {user_statistic}
            Draw :: {draw_statistic}
            ''')
        break