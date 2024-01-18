'''
Завдання 1
Користувач вводить із клавіатури рядок. Перевірте, чи є введений рядок паліндромом. Паліндром — слово або текст, яке читається однаково зліва направо і справа наліво. Наприклад, кок; кіт утік; я несу гусеня; радар; зараз. Або російською — А роза упала на лапу Азора; доход; А буду я у дуба.
'''

text = 'Введіть ваше речення: '

text = text.replace(' ', '').lower()

palindrome = False

if text == text[::-1]:
    palindrome = True
else:
    palindrome = False
    
if palindrome:
    print("Введений рядок - паліндром.")
else:
    print("Введений рядок не є паліндромом.")

'''
Завдання 2
Користувач вводить із клавіатури певний текст, після чого користувач вводить список зарезервованих слів. Необхідно знайти в тексті всі зарезервовані слова і змінити їхній регістр на верхній. Вивести на екран змінений текст.
'''

message = input('Enter your sentence: ')

words = []

while True:
    word = input('Enter the word: ')
    words.append(word)
    exit = input('Do you want to add another word? YES = y NO = n: ')
    exit = exit.lower()
    if exit != 'y':
        break

for i in range(len(words)):
    j = words[i].capitalize()
    message = message.replace(words[i], j)
print()
print(message)
print()

'''
Завдання 3
Є деякий текст. Порахуйте в цьому тексті кількість речень і виведіть на екран отриманий результат.
'''

message = input('Введіть речення для перевірки: ')

count = message.count('.')

print(f'В даному тесті є {count} речень.')