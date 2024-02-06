'''
Завдання 1
Напишіть функцію, що обчислює суму елементів списку цілих. Список передається як параметр.
'''

def summa(*args):
    res = 0
    for i in args:
        res += int(i)
    return res


numbers = input('Ведіть числа через пробіл: ').split(' ')
res = summa(*numbers)
print(f"Сума чисел: {res}")


'''
Завдання 2
Напишіть функцію для знаходження максимуму в списку цілих. Список передається як параметр.
'''

def maxNum(*args):
    res = 0
    for i in args:
        if int(i) > res:
            res = int(i)
    return res

numbers = input('Ведіть числа: ').split(' ')
res = maxNum(*numbers)
print(f"Максимальне число: {res}")

'''
Завдання 3
Напишіть функцію, що визначає кількість парних, непарних, додатних, від'ємних елементів списку цілих. Список передається як параметр.
'''

numbers = input('Ведіть числа: ').split(' ')
numbers = [int(num) for num in numbers]

even = len(list(filter(lambda x: x % 2 == 0, numbers)))
odd = len(list(filter(lambda x: x % 2 != 0, numbers)))

print("Кількість парних чисел:", even)
print("Кількість непарних чисел:", odd)

'''
Завдання 4
Напишіть функцію, що перевертає вміст списку цілих.
'''

def revers(*args):
    for i in args[::-1]:
        print(int(i), end=' ')
    print()

numbers = input('Ведіть числа: ').split(' ')
revers(*numbers)

'''
Завдання 5
Напишіть функцію, яка шукає деяке число у списку цілих.
'''

numbers = input('Ведіть числа: ').split(' ')
numbers = [int(num) for num in numbers]
num = int(input('Яке число знайти?: '))

search = list(filter(lambda x: x == num, numbers))

if search:
    print(f"Число {num} знайдено в списку.")
else:
    print(f"Число {num} не знайдено в списку.")

'''
Завдання 6
Напишіть функцію, що обчислює факторіал кожного елемента списку цілих. Функція повертає новий список, який містить отримані факторіали.
'''
def factorial(*args):
    result = []
    for num in args:
        fact = 1
        for i in range(1, int(num) + 1):
            fact *= i
        result.append(fact)
    return result

numbers = input('Введіть числа: ').split(' ')

factorials = factorial(*numbers)
print("Факторіали:", factorials)

