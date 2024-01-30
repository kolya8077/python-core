import random

arr = []

for i in range(1,100):
    arr.append(random.randint(-100,100))
'''
Завдання 1
У списку цілих, заповненому випадковими числами обчислити:

суму від'ємних чисел;
суму парних чисел;
суму непарних чисел;
добуток елементів з індексами кратними 3;
добуток елементів між мінімальним і максимальним елементом;
суму елементів, що знаходяться між першим та останнім додатними елементами. 
'''

negative = 0
paired = 0
odd = 0
multiple_3 = 1
min_max = 1
positive = 0

for i in arr:
    if i < 0:
        negative+= i
    if i % 2 == 0:
        paired += i
    if i % 2 != 0:
        odd += i
    if i % 3 == 0:
        multiple_3 *= i
        

min_index = arr.index(min(arr))
max_index = arr.index(max(arr))

if min_index > max_index:
    min_index, max_index = max_index, min_index

while min_index <= max_index:
    min_max *= arr[min_index]
    min_index += 1

max_num = 0
min_num = 100

for i in arr:
    if i > 0:
        if i < min_num:
            min_num = i
        elif i > max_num:
            max_num = i

min_index, max_index = arr.index(min_num), arr.index(max_num)

if min_index > max_index:
    min_index, max_index = max_index, min_index

while min_index <= max_index:
    positive += arr[min_index]
    min_index += 1

print("Список випадкових чисел:", arr)
print("Сума від'ємних чисел:", negative)
print("Сума парних чисел:", paired)
print("Сума непарних чисел:", odd)
print("Добуток елементів з індексами кратними 3:", multiple_3)
print("Добуток елементів між мінімальним і максимальним елементом:", min_max)
print("Сума елементів між першим та останнім додатними елементами:", positive)

'''
Завдання 2
Є список цілих, заповнений випадковими числами. На підставі даних цього масиву потрібно:

створити список цілих, що містить тільки парні числа з першого списку;
створити список цілих, що містить тільки непарні числа з першого списку;
створити список цілих, що містить тільки від'ємні числа з першого списку;
створити список цілих, що містить тільки додатні числа з першого списку.
'''

paired = 0
odd = 0
negative = 0
positive = 0

for i in arr:
    if i % 2 == 0:
        paired += i 
    if i % 2 != 0:
        odd += i
    if i < 0:
        negative += i
    if i > 0:
        positive += i
print()
print("Список парних чисел:", paired)
print("Список непарних чисел:", odd)
print("Список від'ємних чисел:", negative)
print("Список додатніх чисел:", positive)
