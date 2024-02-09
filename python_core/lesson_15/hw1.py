import random

arr1 = [ random.randint(1,100) for i in range(25)]
arr2 = [ random.randint(1,100) for i in range(25)]
print('Список 1 =',arr1)
print('Список 2 =',arr2)
'''
Завдання 1
Напишіть функцію, що обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається з функції.
'''

# def mult(*args):
#     summa = 1
#     for num in args:
#         summa *= int(num)
#     return summa

# print(mult(*arr1))

'''
Завдання 2
Напишіть функцію для знаходження мінімуму в списку цілих. Список передається як параметр. Отриманий результат повертається з функції.
'''

# def minimum(*args):
#     value = 999
#     for i in args:
#         if value > i:
#             value = i
#     return value

# print(minimum(*arr1))

'''
Завдання 3
Напишіть функцію, що визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається з функції.
'''

# def prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def count(*args):
#     count = 0
#     for num in args:
#         if prime(num):
#             count += 1
#     return count

# numbers = arr1
# result = count(*numbers)
# print("Кількість простих чисел у списку:", result)

'''
Завдання 4
Напишіть функцію, що видаляє зі списку цілих деяке задане число. З функції потрібно повернути кількість видалених елементів.
'''

