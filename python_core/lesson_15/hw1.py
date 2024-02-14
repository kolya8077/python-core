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

# def delete_elements(new, arr1):
#     deleted_elements = list(filter(lambda x: x != new, arr1))
#     count = len(arr1) - len(deleted_elements)
#     arr1[:] = deleted_elements
#     return count

# print("Список:", arr1)
# number = int(input('Яке число бажаєте видалити?: '))
# deleted_count = delete_elements(number, arr1)
# print("Кількість видалених елементів:", deleted_count)
# print("Оновлений список:", arr1)

'''
Завдання 5
Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
'''

# def merge_lists(list1, list2):
#     return list1 + list2

# print("Об'єднаний список:", merge_lists(arr1, arr2))

'''
Завдання 6
Напишіть функцію, що обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр, список теж передається як параметр. Функція повертає новий список, що містить отримані результати.
'''

def power_up(arr, power):
    return [num ** power for num in arr]


numbers = arr1
power = int(input('Ведіть число до якого ступіня піднести: '))

print(f"Список чисел піднесений до степеня {power}: {power_up(numbers, power)}")
