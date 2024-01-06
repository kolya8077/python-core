from InquirerPy import prompt

while True:
    print('Який трикутник відобразити?')
    questions = [
        {"type": "list", "message": "Оберіть трикутник:", "name": "value", "choices": ['1. а;', '2. б;', '3. в;', '4. г;', '5. д;', '6. е;', '7. ж;', '8. з;', '9. и;', '10. к;']},
    ]

    answers = prompt(questions)['value']

    match answers: 
        case '1. а;':
            n = 7
            print('_' * 17)
            for i in range(n, 0, -1):
                print('| ', end='')
                for j in range(n - i):
                    print(' ', end=' ')
                for k in range(i):
                    print('*', end=' ')
                print('|')
            print('-' * 17)
        case '2. б;':
            n = 6
            print('_' * 17)
            for i in range(n, 0, -1):
                print('| ', end='')
                for j in range(n - i + 1 ):
                    print('*', end=' ')
                for k in range(i):
                    print(' ', end=' ')
                print('|')
            else:
                print('| ', '* '*7, '|', sep='')
            print('-' * 17)
        case '3. в;':
            n = 7
            print('_' * 17)
            for i in range(n, 0, -2):
                print('| ', end='')
                for j in range((n - i) // 2):
                    print(' ', end=' ')
                for k in range(i):
                    print('*', end=' ')
                for j in range((n - i) // 2):
                    print(' ', end=' ')
                print('|')
            for i in range(1, n + 1, 2):
                print('| ', end='')
                for j in range(n):
                    print(' ', end=' ')
                print('|')
            print('-' * 17)
        case '4. г;':
            n = 7
            print('_' * 17)
            for i in range(n, 0, -2):
                print('| ', end='')
                for j in range(n):
                    print(' ', end=' ')
                print('|')

            for i in range(1, n + 1, 2):
                print('| ', end='')
                
                for j in range((n - i) // 2):
                    print(' ', end=' ')
                for k in range(i):
                    print('*', end=' ')
                for j in range((n - i) // 2):
                    print(' ', end=' ')
                print('|')
                
            print('-' * 17)
        case '5. д;':
            n = 7
            print('_' * 17)
            for i in range(n, 0, -2):
                print('| ', end='')
                for j in range((n - i) // 2):
                    print(' ', end=' ')
                for k in range(i):
                    print('*', end=' ')
                for j in range((n - i) // 2):
                    print(' ', end=' ')
                print('|')

            for i in range(1, n + 1, 2):
                print('| ', end='')
                
                for j in range((n - i) // 2):
                    print(' ', end=' ')
                for k in range(i):
                    print('*', end=' ')
                for j in range((n - i) // 2):
                    print(' ', end=' ')
                print('|')
                
            print('-' * 17)
        case '6. е;':
            n = 5
            print('_' * 12)
            for i in range(1, n + 1):
                print('|', end='')
                for j in range(i):
                    print('*', end='')
                for j in range(2 * (n - i)):
                    print(' ', end='')
                for j in range(i):
                    print('*', end='')
                print('|')
                
            for i in range(n - 1, 0, -1):
                print('|', end='')
                for j in range(i):
                    print('*', end='')
                for j in range(2 * (n - i)):
                    print(' ', end='')
                for j in range(i):
                    print('*', end='')
                print('|')
            print('-' * 12)
        case '7. ж;':
            n = 5
            print('_' * 12)
            for i in range(1, n + 1):
                print('|', end='')
                for j in range(i):
                    print('*', end='')
                for j in range(2 * (n - i)):
                    print(' ', end='')
                for j in range(i):
                    print(' ', end='')
                print('|')
                
            for i in range(n - 1, 0, -1):
                print('|', end='')
                for j in range(i):
                    print('*', end='')
                for j in range(2 * (n - i)):
                    print(' ', end='')
                for j in range(i):
                    print(' ', end='')
                print('|')
            print('-' * 12)
        case '8. з;':
            n = 5
            print('_' * 12)
            for i in range(1, n + 1):
                print('|', end='')
                for j in range(i):
                    print(' ', end='')
                for j in range(2 * (n - i)):
                    print(' ', end='')
                for j in range(i):
                    print('*', end='')
                print('|')
                
            for i in range(n - 1, 0, -1):
                print('|', end='')
                for j in range(i):
                    print(' ', end='')
                for j in range(2 * (n - i)):
                    print(' ', end='')
                for j in range(i):
                    print('*', end='')
                print('|')
            print('-' * 12)
        case '9. и;':
            n = 7
            print('_' * 17)
            for i in range(n, 0, -1):
                print('| ', end='')
                for j in range(n):
                    if i > j:
                        print('*', end=' ')
                    else:
                        print(' ', end=' ')
                print('|')
            print('-' * 17)
        case '10. к;':
            n = 7
            print('_' * 17)
            for i in range(n, 0, -1):
                print('| ', end='')
                for j in range(n):
                    if (i-1) > j:
                        print(' ', end=' ')
                    else:
                        print('*', end=' ')
                print('|')
            print('-' * 17)
    
    questions = [
        {"type": "list", "message": "Продовжуємо?:", "name": "value", "choices": ['Так', 'Ні']},
    ]

    answers = prompt(questions)['value']
    
    match answers:
        case 'Так':
            continue
        case 'Ні':
            break