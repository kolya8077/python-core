'''
Завдання 1
Напишіть програму, яка запитує у користувача імʼя та вік. Після отримання даних
програма повинна виводити привітання у форматі: "Привіт, {імʼя}! Твій вік — {вік}".
Обробіть виняток, що виникає при введенні некоректного віку (вік < 0 або вік > 130),
і виведіть повідомлення про помилку.
'''

# name = None
# age = None

# while name == None or age == None:
#     try:
#         name = input('Обізвіть користувача: ')
#         age = int(input('Ведіть вік користувача: '))
#         if age < 0:
#             raise Exception("Помилка у віці! вік < 0!")
#         if age >= 130:
#             raise Exception("Помилка у віці! вік > 130!")
#     except ValueError:
#         print("Помилка введення!!! Потрібно ввести число")
#         age = None
#     except Exception as ex:
#         print(ex)
#         age = None
# print(f"Привіт, {name}! Твій вік - {age}")

'''
Завдання 2
Реалізуйте перше завдання через функцію. Функція повинна приймати імʼя і вік як
параметри і повертати відформатований рядок. Перевірка коректності отриманих
даних повинна бути всередині функції. Створіть дві версії реалізації функції:
• Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться
зовні;
• Друга версія обробляє виняток усередині функції.
'''

# def format(name, age):
#     print(f"Привіт, {name}! Твій вік - {age}")

# name = None
# age = None

# while True:
#     try:
#         name = input('Обізвіть користувача: ')
#         age = int(input('Ведіть вік користувача: '))
#         if age < 0:
#             raise Exception("Помилка у віці! вік < 0!")
#         if age >= 130:
#             raise Exception("Помилка у віці! вік > 130!")
#         format(name, age)
#         break
#     except ValueError:
#         print("Помилка введення!!! Потрібно ввести число")
#     except Exception as ex:
#         print(ex)

#============================================================================

# def fullFormat(name, age):
#         try:
#             age = int(age)
#             if age < 0:
#                 raise Exception("Помилка у віці! Вік < 0!")
#             if age >= 130:
#                 raise Exception("Помилка у віці! Вік > 130!")

#             return f"Привіт, {name}! Твій вік - {age}"
#         except ValueError:
#             print("Помилка введення!!! Потрібно ввести число")

# name = None
# age = None

# while True:
#     try:
#         name = input('Обізвіть користувача: ')
#         age = int(input('Ведіть вік користувача: '))
#         result = fullFormat(name, age)
#         print(result)
#         break
#     except Exception as ex:
#         print(ex)

'''
Завдання 3
Напишіть програму, яка дозволяє користувачеві ввести з клавіатури набір додатних
(число більше нуля) чисел. Числа необхідно накопичувати у списку. Після отрима-
ння всіх значень програма повинна проаналізувати дані. У разі виявлення відʼємного
значення програма має згенерувати виняток. Якщо всі значення у списку позитивні,
програма має повернути на екран суму всіх чисел списку.
Згенерований виняток має бути оброблений кодом програми.
'''



arr = []
result = 0
summa = 0


while True:
    try:
        if len(arr) > 0:
            question = input('Бажаєте продовжитти вводити? ТАК = y, НІ = n: ')
            match question:
                case 'y':
                    pass
                case "n":
                    result = summa(arr)
                    if result == None:
                        result = 'Виявлено відємне число.'
                    break
                case _:
                    raise Exception("Error")
        
        num = int(input('Введіть додатнє число: '))
        arr.append(num)
            
    except ValueError:
        print("Помилка введення!!! Потрібно ввести число")
    except Exception as ex:
        print(ex)

try:
    for i in arr:
        if i > 0:
            for i in arr:
                summa += i
        else:
            raise Exception("виявлення відʼємного значення")
except ValueError:
        print("Помилка введення!!! Потрібно ввести число")
except Exception as ex:
    print(ex)

print(arr)
print(result)

'''
Завдання 4
Реалізуйте третє завдання через функцію. Функція повинна приймати список як ар-
гумент і повертати суму елементів списку. Перевірка коректності отриманих даних
повинна бути всередині функції. Створіть дві версії реалізації функції:
• Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться
зовні;
• Друга версія обробляє виняток усередині функції.
'''

def summa(arr):
    summa = 0
    try:
        for i in arr:
            if i > 0:
                for i in arr:
                    summa += i
            else:
                raise Exception("виявлення відʼємного значення")
        return summa
    except ValueError:
            print("Помилка введення!!! Потрібно ввести число")
    except Exception as ex:
        print(ex)

arr = []
result = 0

while True:
    try:
        if len(arr) > 0:
            question = input('Бажаєте продовжитти вводити? ТАК = y, НІ = n: ')
            match question:
                case 'y':
                    pass
                case "n":
                    result = summa(arr)
                    if result == None:
                        result = 'Виявлено відємне число.'
                    break
                case _:
                    raise Exception("Error")
        
        num = int(input('Введіть додатнє число: '))
        arr.append(num)
            
    except ValueError:
        print("Помилка введення!!! Потрібно ввести число")
    except Exception as ex:
        print(ex)

print(arr)
print(result)