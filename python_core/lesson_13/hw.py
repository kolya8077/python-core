'''
Завдання 1
Напишіть функцію, яка відобразить на екрані такий форматований текст:

"Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself."
Bill Gates
'''
def text():
    print(f'''
    \033[30m"Don't compare yourself with anyone in this world…\033[0m
    \033[31mif\033[0m you \033[31mdo\033[0m so, you are insulting yourself.\033[30m"\033[0m
    Bill Gates
    ''')

text()

'''
Завдання 2
Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.
'''

def paired(num1, num2):
    for i in range(num1, num2+1):
        if i % 2 == 0:
            print(i, end=' ')
    print()

num1 = int(input('Вкажіть початкове число: '))
num2 = int(input('Вкажіть кінечне число: '))
paired(num1, num2)


'''
Завдання 3
Напишіть функцію, яка відображає порожній або заповнений квадрат з певного символу. Функція приймає як параметри довжину сторони квадрата, символ і змінну логічного типу:

якщо вона дорівнює True, квадрат заповнений;
якщо — False, квадрат порожній.
'''

def symb(symbol, length):
    for i in range(length):
        print(symbol, end=' ')
    print()

def square(length, symbol, bl):
    symb(symbol, length)
    for i in range(length-2):
        print(symbol, end=' ')
        if bl == True:
            for j in range(length-2):
                print(symbol, end=' ')
        elif bl == False:
            for j in range(length - 2):
                print(' ', end=' ')
        print(symbol, end='')
        print()
    symb(symbol, length)


length = int(input('Ведіть довжину квадрату: '))
symbol = input('Введіть обраний спец символ: ')
bl = ''
while True:
    bl = input('Квадрат повинен бути заповнений чи пустий? y - заповнений, n - порожній: ')
    bl = bl.lower()
    match bl:
        case "y": 
            bl = True
            break
        case "n":
            bl = False
            break
        case _:
            print('Помилка, введіть коректну літеру.')
            continue

square(length, symbol, bl)

'''
Завдання 4
Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри.
'''

def minNum(arr):
    return min(arr)

arr = []

for i in range(5):
    num = int(input(f'Ведіть число {i+1}: '))
    arr.append(num)

print(minNum(arr))

'''
Завдання 5
Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні. Межі діапазону передаються як параметри. Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх треба поміняти місцями.
'''

def product(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    
    res = 1
    
    while num1 <= num2:
        res *= num1
        num1 +=1
    return res

num1 = int(input('Введіть число: '))
num2 = int(input('Введіть число: '))

print('Добуток чисел: ', product(num1, num2))

'''
Завдання 6
Напишіть функцію, яка рахує кількість цифр у числі. Число передається як параметр. З функції потрібно повернути отриману кількість цифр. Наприклад, якщо передали 3456, кількість цифр буде 4.
'''

def numbers(num):
    return len(num)

num = input("Введіть число: ")

print(numbers(num))

'''
Завдання 7
Напишіть функцію, яка перевіряє, чи є число паліндромом. Число передається як параметр. Якщо число є паліндромом, потрібно повернути з функції true, якщо ні — false.

Паліндром — це число, у якого перша частина цифр рівноцінна другій дзеркально відображеній частині цифр. Наприклад, 123321 — паліндром (перша частина – 123, друга частина – 321, повернувши яку отримаємо 123). 546645 — паліндром, а 421987 — не паліндром.
'''

def palindrom(number):
    arr = [int(i) for i in number]
    for i in range(len(arr)//2):
        if arr[i] == arr[-i-1]:
            continue
        else:
            print("Число не є палндромом!")
            return 
    print('Число є палндромом!')
    
number = input('Ведіть число: ')
palindrom(number)

