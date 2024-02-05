import random

arr = [random.randint(1, 100) for i in range(1,20)]

'''
"Don't let the noise of others' opinions
drown out your own inner voice."
Steve Jobs
'''

def colorsText():
    print(f'''\033[34m"Don't let the noise of others' opinions
drown out your own inner voice.\33[0m"
\033[33mSteve Jobs\033[0m''')

colorsText()

'''
Завдання 2
Напишіть функцію, яка приймає два числа як параметр і відображає всі непарні чи-
сла між ними.
'''

def oddNum(arr):
    numbers = []
    for i in arr:
        if i % 2 != 0:
            numbers.append(i)
    return numbers

print(oddNum(arr))


'''
Завдання 3
Напишіть функцію, яка відображає горизонтальну або вертикальну лінію з деякого символу. Функція приймає як параметр довжину лінії, напрямок, символ.
'''

def line(length, direction, symbol):
    match direction:
        case 1:
            print(symbol * length)
        case 2:
            for _ in range(length):
                print(symbol)

length = int(input('Вкажіть довжину: '))
direction = int(input('Вертикально - 1, горизонтально - 2: '))
symbol = input('Вкажіть символ: ')

line(length, direction, symbol)


'''
Завдання 4
Напишіть функцію, яка повертає максимальне з чотирьох чисел. Числа передаються як параметри.
'''

def max4(num1, num2, num3, num4):
    return max(num1, num2, num3, num4)

num1 = int(input('Введіть число: '))
num2 = int(input('Введіть число: '))
num3 = int(input('Введіть число: '))
num4 = int(input('Введіть число: '))

result = max4(num1, num2, num3, num4)
print(f'Максимальне число: {result}')

'''
Завдання 5
Напишіть функцію, яка повертає суму чисел у вказаному діапазоні. Межі діапазону передаються як параметри.
'''


def summaNum(arr, start, end):
    summa = 0
    for i in range(start, end + 1):
        summa += arr[i]
    return summa

print(summaNum(arr, 3,5))

'''
Завдання 6
Напишіть функцію, яка перевіряє, чи є число простим. Число передається як параметр. Якщо число просте потрібно повернути з методу true, в іншому разі — false.
'''

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

num = int(input('Введіть число: '))
result = is_prime(num)

if result:
    print(f'{num} - просте число')
else:
    print(f'{num} - не просте число')

'''
Завдання 7
Напишіть функцію, яка перевіряє, чи є шестизначне число "щасливим". Число передається як параметр. Якщо число щасливе потрібно повернути з функції true, якщо ні — false.

Щасливе шестизначне число — це число, у якого сума перших трьох цифр дорівнює сумі трьох інших цифр. Наприклад, 123420 — щасливе, бо 1+2+3 = 4+2+0, а 723422 — нещасливе, тому що 7+2+3 != 4+2+2.
'''

def isHappyNumber(number):
    number = str(number)

    if len(number) != 6:
        return False

    first = [int(digit) for digit in number[:3]]
    second = [int(digit) for digit in number[3:]]

    return sum(first) == sum(second)

num = int(input('Введіть шестизначне число: '))

if isHappyNumber(num):
    print(f'{num} - щасливе число')
else:
    print(f'{num} - нещасливе число')
