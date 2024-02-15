'''
Завдання 1
Написати рекурсивну функцію знаходження ступеня числа.
'''

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent - 1)

# number = int(input('Введіть число яке потрібно привести до ступення: '))
# power = int(input('Введіть число до якого степіння підвести: '))
# result = power(number, power)
# print(f"{number}^{power} = {result}")


'''
Завдання 2
Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b. Користувач вводить a і b. Проілюструйте роботу функції прикладом.
'''

'''
def summa(a, b):
    if a == b:
        return a
    return a + summa(a + 1, b)

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

result = summa(a, b)
print(f"Сума всіх чисел в діапазоні від {a} до {b} дорівнює {result}.")
'''

'''
Завдання 3
Написати рекурсивну функцію, яка виводить N зірок у ряд. Число N задає користувач. Проілюструйте роботу функції прикладом.
'''

# def print_stars(N):
#     if N == 0:
#         return
    
#     print("*", end="")
#     print_stars(N - 1)

# N = int(input("Введіть число N: "))

# print()
# print_stars(N)

'''
Завдання 5
Напишіть рекурсивну функцію, що отримує список зі 100 цілих чисел, отриманих випадковим чином, і знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.
'''

import random

arr = [random.randint(1, 100) for _ in range(100)]

def min_sum_position(arr, start=0):
    if len(arr) < 10:
        return -1

    if start + 10 > len(arr):
        return -1

    current_sum = sum(arr[start:start+10])

    min_position = min_sum_position(arr, start+1)
    if min_position == -1:
        return start
    elif sum(arr[min_position:min_position+10]) < current_sum:
        return min_position
    else:
        return start

print("Початковий список:", arr)
position = min_sum_position(arr)
if position != -1:
    print("Позиція, з якої починається послідовність з 10 чисел з мінімальною сумою:", position)
    print("Ці числа:", arr[position:position + 10])
else:
    print("В списку менше ніж 10 чисел, отже такої послідовності немає.")



'''
Завдання 6
Написати функцію, яка приймає дві дати (тобто функція приймає шість параметрів) і обчислює різницю в днях між цими датами. Для виконання цього завдання необхідно також написати функцію, яка визначає, чи є рік високосним.
'''

# def years(day, month, year):
#     if((year % 4==0) and (year % 100 !=0) or ( year % 400==0)):
#         return day + months1[month]
#     elif((year % 4==0) and (year % 100 !=0) or ( year % 400==0)):
#         return day + months2[month]

# months1 = [31,29,31,30,31,31,30,31,30,31,30,31]
# months2 = [31,28,31,30,31,31,30,31,30,31,30,31]
# days = []

# for i in range(2):
#     print(f'{i+1} дата:')
#     day = int(input("Введіть день першої дати: "))
#     month = int(input("Введіть місяць першої дати: "))
#     year = int(input("Введіть рік першої дати: "))
#     days.append(years(day, month, year))

# ollDay = days[1] - days[0]

# print(f"Кількість днів між датами: {ollDay} днів.")