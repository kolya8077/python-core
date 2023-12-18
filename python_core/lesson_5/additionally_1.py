'''
Завдання 1
Користувач вводить із клавіатури два числа. Потрібно показати всі числа у вказаному діапазоні.
'''

# numOne = int(input('ВВедіть перше число: '))
# numTwo = int(input('ВВедіть друге число: '))

# while numOne < numTwo:
#     print(numOne, end=' ')
#     numOne += 1

'''
Завдання 2
Користувач вводить із клавіатури два числа. Потрібно показати всі непарні числа у вказаному діапазоні.
'''

# numOne = int(input('ВВедіть перше число: '))
# numTwo = int(input('ВВедіть друге число: '))

# while numOne <= numTwo:
#     if numOne % 2 == 0:
#         numOne += 1
#     else:
#         print(numOne)
#         numOne += 1

'''
Завдання 3
Користувач вводить із клавіатури два числа. Потрібно показати всі парні числа у вказаному діапазоні.
'''

# numOne = int(input('ВВедіть перше число: '))
# numTwo = int(input('ВВедіть друге число: '))

# while numOne <= numTwo:
#     if numOne % 2 == 0:
#         print(numOne)
#     numOne += 1

'''
Завдання 4
Користувач вводить із клавіатури два числа. Потрібно показати всі числа у вказаному діапазоні в порядку убування.
'''

# numOne = int(input('ВВедіть перше число: '))
# numTwo = int(input('ВВедіть друге число: '))

# while numTwo >= numOne:
#   numTwo -= 1
#   print(numTwo)

'''
Завдання 5
Користувач вводить із клавіатури два числа. Потрібно показати всі непарні числа у вказаному діапазоні. Якщо межі діапазону вказані неправильно, потрібно провести нормалізацію меж. Наприклад, користувач ввів 33 і 13. Потрібна нормалізація, після якої початок діапазону стане дорівнювати 13, а кінець — 33.
'''

# numOne = int(input('ВВедіть перше число: '))
# numTwo = int(input('ВВедіть друге число: '))

# if numOne > numTwo:
#     num = numOne
#     numOne = numTwo
#     numTwo = num
#     print(numTwo)
#     while numOne <= numTwo:
#         if numOne % 2 == 0:
#             numOne += 1
#         else:
#             print(numOne)
#             numOne += 1
# else: 
#     while numOne <= numTwo:
#         if numOne % 2 == 0:
#             numOne += 1
#         else:
#             print(numOne)
#             numOne += 1