'''
Модуль 2. Змінні та типи даних
Частина 2
'''

# Завдання 1
# Користувач із клавіатури вводить двозначне число. Наприклад, 26. Потрібно показати на різних рядках значення першого і другого розряду. У цьому разі це виглядатиме так:

# 2
# 6

# num = int(input('Введіть число')) 

# num1 = num // 10
# num2 = num % 10

# print(f'{num1}\n{num2}')

# Завдання 2
# Користувач із клавіатури вводить тризначне число. Наприклад, 891. Потрібно показати на різних рядках значення першого, другого і третього розряду. Також потрібно показати на окремому рядку суму цих трьох чисел. У цьому разі це виглядатиме так:

# 8
# 9
# 1
# 18

# num = int(input('Введіть число')) 

# num1 = num // 100
# num2 = num % 100 // 10
# num3 = num % 10
# suma = num1 + num2 + num3

# print(f'{num1}\n{num2}\n{num3}\n{suma}')

# Завдання 3
# Користувач вводить із клавіатури дві цифри. Необхідно створити число, що містить ці цифри. Наприклад, якщо з клавіатури введено 9, 7, тоді потрібно сформувати число 97.

# num1 = int(input('Введіть перше число: '))
# num2 = int(input('Введіть друге число: '))

# res = num1 * 10 + num2

# print('Ваше число: ', res)

# Завдання 4
# Користувач вводить із клавіатури температуру за шкалою Цельсія. Потрібно перевести температуру в градуси за Фаренгейтом і вивести на екран.

# num = int(input('Цельсій: '))

# suma = num * 1.8 + 32

# print('Значеня у фарінгейтах =', suma)