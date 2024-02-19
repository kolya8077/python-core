'''
Завдання 1
Напишіть програму, яка дозволяє користувачеві обчислити частку (ділення одного числа на інше) двох чисел. Програма приймає два значення з клавіатури і повертає результат операції на екран. Обробіть виняток, що виникає під час ділення на нуль, і виведіть повідомлення про помилку.
'''

while True:
    try:    
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        if num2 == 0:
            raise ZeroDivisionError("You can't divide by zero!")
        result = num1 / num2
        print(f"Result: {result}")
        break 
    except ValueError:
        print("Error: You need to enter a valid number.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

'''
Завдання 2
Реалізуйте перше завдання через функцію. Функція повинна приймати два параметри і відображати результат ділення на екран. Створіть дві версії реалізації функції:

Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції.
'''

'''перша версія'''

def divide_numbers(num1, num2):
    return num1 / num2

while True:
    try:    
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        result = divide_numbers(num1, num2)
        print(f"Result: {result}")
        break 
    except ValueError:
        print("Error: You need to enter a valid number.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


'''друга версія'''

def divide_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        raise ZeroDivisionError("You can't divide by zero!") from e

while True:
    try:    
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        result = divide_numbers(num1, num2)
        print(f"Result: {result}")
        break 
    except ValueError:
        print("Error: You need to enter a valid number.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

'''
Завдання 3
Напишіть програму, яка приймає рядок і намагається перетворити його на число.

Обробіть виняток, що виникає при неможливості перетворення, і виведіть повідомлення про помилку.
'''

while True:
    try:
        user_input = input("Enter a number: ")
        number = float(user_input)
        print(f"Number: {number}")
        break
    except ValueError:
        print("Error: Unable to convert the input to a number. Please enter a valid number.")

'''
Завдання 4
Реалізуйте третє завдання через функцію. Функція повинна приймати рядок і відображати результат перетворення на екран. Створіть дві версії реалізації функції:

Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції.
'''

'''перша версія'''

def convert_to_number(user_input):
    return float(user_input)

while True:
    try:
        user_input = input("Enter a number: ")
        number = convert_to_number(user_input)
        print(f"Number: {number}")
        break
    except ValueError:
        print("Error: Unable to convert the input to a number. Please enter a valid number.")


'''друга версія'''

def convert_to_number(user_input):
    try:
        return float(user_input)
    except ValueError as e:
        raise ValueError("Unable to convert the input to a number.") from e

while True:
    try:
        user_input = input("Enter a number: ")
        number = convert_to_number(user_input)
        print(f"Number: {number}")
        break
    except ValueError as e:
        print(f"Error: {e}")
