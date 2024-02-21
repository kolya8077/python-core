import re

'''
Завдання 1
Маємо текстовий файл. Створіть новий файл та перепишіть з вихідного файлу всі слова, що складаються не менше, ніж із семи літер.
'''

# url1 = 'files/url1.txt'

# with open(url1) as file:
#     line = file.read()

# words = re.split(r'\W', line)
        
# with open(url1, 'w') as file:
#     for word in words:
#         if len(word) >= 7:
#             file.write(word + '\n')

'''
Завдання 2
Маємо текстовий файл. Перепишіть його рядки в інший файл. Порядок рядків у другому файлі має збігатися з порядком рядків у заданому файлі. 
'''

# input_file = 'files/url2.txt'
# output_file = 'files/url3.txt'

# with open(input_file, 'r') as input_f:
#     with open(output_file, 'w') as output_f:
#         for line in input_f:
#             output_f.write(line)

'''
Завдання 3
Маємо текстовий файл. Перепишіть його рядки в інший файл. Порядок рядків у другому файлі має бути зворотним до порядку рядків у заданому файлі.
'''

# input_file = 'files/url2.txt'
# output_file = 'files/url4.txt'


# with open(input_file, 'r') as input_f:
#     lines = input_f.readlines()

# with open(output_file, 'w') as output_f:
#     for line in lines[::-1]:
#         output_f.write(line)

'''
Завдання 4
Маємо текстовий файл. Додайте до нього рядок із дванадцяти зірочок (************), помістивши його після останнього з рядків, в яких немає коми. Якщо таких рядків немає, додайте новий після всіх рядків файлу. Результат запишіть до іншого файлу.
'''

url = 'files/url5.txt'

with open(url, 'r') as file:
    lines = file.readlines()

last_line_index = -1
for i, line in enumerate(lines):
    if ',' in line:
        last_line_index = i
        break

stars_line = '************\n'

if last_line_index != -1:
    lines.insert(last_line_index + 1, stars_line)
else:
    lines.append(stars_line)

with open(url, 'w') as file:
    file.writelines(lines)

'''
Завдання 5
Маємо текстовий файл. Підрахуйте кількість слів, що починаються з символу, який задає користувач.
'''

# url = 'files/url5.txt'

# count = 0
# leter = input('Введіть літеру: ').lower()

# with open(url, 'r') as file:
#     line = file.read()
    
# words = re.split(r'\W+', line)
        
# for word in words:
#     if word != '':
#         l = word[0].lower()
#         if l == leter:
#             count += 1
# print(count)

'''
Завдання 6
Маємо текстовий файл. Перепишіть до іншого файлу всі його рядки замінюючи в них символ * на символ &, і навпаки. 
'''

# with open('./files/url6.txt')as file:
#     text = file.read()
#     with open('./files/url7.txt', 'w') as file:
#         for word in text:
#             for leter in word:
#                 if leter == '*':
#                     file.write('&')
#                 elif leter == '&':
#                     file.write('*')
#                 else:
#                     file.write(leter)

'''
Завдання 7
Маємо масив рядків. Запишіть їх у файл, розташувавши кожен елемент масиву на окремому рядку із збереженням порядку. 

Завдання 8
Маємо масив рядків. Запишіть їх у файл, розташувавши кожен елемент масиву на окремому рядку із збереженням порядку. 
'''

# random_words = [
#     "Сьогодні гарний день.",
#     "Я люблю читати книги.",
#     "Погода за вікном дуже холодна.",
#     "Мій улюблений колір - синій.",
#     "Життя прекрасне пригоди.",
#     "У вихідні я зазвичай готую.",
#     "Ми вчимо нові речі кожен день.",
#     "Моя собака завжди рада мене бачити.",
#     "Футбол - це мій улюблений вид спорту.",
#     "Місцева кав'ярня має найкращу каву у місті."
#     "Цей масив згенерував chatGPT якщо що))"
#     "Тут був Коля. Це на випадок якщо Сірьожа зкопіпастить мій код)))"
# ]

# with open('./files/url8.txt', 'w') as file:
#     for i in random_words:
#         file.write(f'{i}\n')


'''
Завдання 9
Маємо текстовий файл. Підрахуйте кількість символів у ньому. 
'''

# with open('./files/url6.txt') as file:
#     text = file.read()

# print(len(text))

'''
Завдання 10
Маємо текстовий файл. Підрахуйте кількість рядків у ньому.
'''

# count = 0

# with open('./files/url5.txt') as file:
#     for i in file:
#         if len(i) >0:
#             count += 1

# print(count)