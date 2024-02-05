import random

arr = []
arr2 = []

for i in range(1,10):
    arr.append(random.randint(1,100))
for i in range(1,10):
    arr2.append(random.randint(1,100))

'''
Завдання
Два списки цілих заповнюються випадковими числами. Необхідно:

сформувати третій список, що містить елементи обох списків;
сформувати третій список, що містить елементи обох списків без пов­торів;
сформувати третій список, що містить елементи спільні для двох списків;
сформувати третій список, що містить тільки унікальні елементи кожного зі списків;
сформувати третій список, що містить тільки мінімальне та максимальне значення кожного зі списків.
'''

arr3 = arr + arr2

without_repetitions = list(set(arr3))

joint = list(set(arr) & set(arr2))

Unique = list(set(arr) ^ set(arr2))

min_max = [min(arr), max(arr), min(arr2), max(arr2)]

print("Список 1:", arr)
print("Список 2:", arr2)
print("Третій список, що містить елементи обох списків:", arr3)
print("Третій список без повторів:", without_repetitions)
print("Третій список, що містить спільні елементи:", joint)
print("Третій список, що містить тільки унікальні елементи кожного зі списків:", Unique)
print("Третій список з мінімальними та максимальними значеннями кожного зі списків:", min_max)