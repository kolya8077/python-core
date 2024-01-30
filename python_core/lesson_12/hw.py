import random

'''
Дано список, заповнений випадковими числами. Збільшити у 2 рази елементи, які
розміщені у списку між найбільшим та найменшим його елементами.
'''

# arr = [random.randint(1,100) for i in range(10)]
# print(arr)
# index_min = arr.index(min(arr))
# index_max = arr.index(max(arr))

# if index_min > index_max:
#     index_min, index_max = index_max, index_min

# while index_min < index_max - 1:
#     index_min+=1
#     arr[index_min] *= 2

# print(arr)


'''
Дано список, заповнений випадковими числами. Поміняти місцями перший елемент 3
другим, третій з четвертим, і т.д. Вивести змінений список на екран.
'''

# arr = [random.randint(1,100) for i in range(10)]
# print(arr)

# for i in range(0, len(arr), 2):
#     arr[i], arr[i + 1] = arr[i + 1], arr[i]
# print(arr)

'''
Дано список, заповнений випадковими числами Знайти у списку значення, що
повторюються.
'''

# arr = [random.randint(1, 10) for _ in range(20)]
# print(arr)

# unique = []
# duplicate = []

# for num in arr:
#     if num in unique:
#         duplicate.append(num)
#     else:
#         unique.append(num)

# if duplicate:
#     print("повторюються значення:", list(duplicate))
# else:
#     print("Значення унікальні.")

'''
У списку зі списками цілих чисел підрахувати суму елементів: у кожному рядку; у кожному
стовпці; одночасно по всіх рядках і всіх стовпцях. Оформити в такий спосіб:
'''

# arr = []

# for i in range(3):
#     rows = []
#     for j in range(4):
#         rows.append(random.randint(10, 20))
#     arr.append(rows)

# for i in range(3):
#     for j in range(4):
#         print(arr[i][j], end=' ')
#     print( '|',sum(arr[i]))
# print('-'*22)

# for i in range(4):
#     suma = 0
#     for j in range(3):
#         suma += arr[j][i]
#     print(suma, end=' ')
# print('|',end=' ')

# suma = 0
# for i in range(3):
#     suma+=sum(arr[i])
# print(suma)