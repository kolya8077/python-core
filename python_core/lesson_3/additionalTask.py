# Завдання 1
# Користувач вводить із клавіатури час у секундах, що минув від початку дня. Залежно від вибору користувача потрібно порахувати скільки годин, хвилин і секунд залишилося до опівночі.

sec = int(input('Час в секундах:'))

time = 86400 - sec
hourse = time // 3600
minute = time % 3600 // 60
secund = time % 60

print(f"До опівночі лишилось {hourse}:{minute}:{secund} годин")

# Завдання 2
# Користувач вводить із клавіатури діаметр кола. Залежно від вибору користувача необхідно порахувати площу або периметр кола.

diameter = float(input("Введіть діаметр кола: "))
operation = input("Введіть 'площа' або 'периметр' для обчислення: ")

if operation == 'площа':
    radius = diameter / 2
    area = 3.14 * (radius ** 2)
    print(f"Площа кола з діаметром {diameter} дорівнює {area}")
elif operation == 'периметр':
    perimeter = 3.14 * diameter
    print(f"Периметр кола з діаметром {diameter} дорівнює {perimeter}")
else:
    print("Будь ласка, введіть 'площа' або 'периметр'")


# Завдання 3
# Користувач вводить із клавіатури вартість однієї ігрової приставки, їхню кількість і відсоток знижки. Залежно від вибору користувача необхідно порахувати загальну суму замовлення або вартість однієї приставки з урахуванням знижки.

price = int(input('Ціна одного товару: '))
amount = int(input('Кількість товару: '))
discount = int(input('Бонусна карта: '))

if discount != 0:
  price = price - (price / 100 * discount)

price *= amount

print(f'Сумма вашого замовлення становить {int(price)} грошей)')

# Завдання 4
# Користувач вводить із клавіатури розмір файлу в гігабайтах і швидкість інтернет-з'єднання в бітах на секунду. Залежно від вибору користувача необхідно порахувати за скільки годин, чи хвилин, чи секунд завантажиться файл.

# Змінив швидкість на кБіт/секунду, тому що захмарні години виходять😅

data = int(input('Введіть обʼєм в Гб: '))
speed = int(input('Введіть швидкість завантаєення в кБіт/сек: '))

speed *= 1000
b = data * 1024 * 1024 * 1024
total = b * 8 // speed

hourse = total // 3600
minute = total % 3600 // 60
secund = total % 60

print(f'Час завантаження {(hourse)}:{minute}:{secund}.')

# Завдання 5
# Користувач із клавіатури вводить кількість годин. Якщо отримане значення знаходиться в діапазоні від 0 до 6, потрібно вивести напис "Good Night", якщо в діапазоні від 6 до 13 — "Good Morning", якщо в діапазоні від 13 до 17 — "Good Day", якщо в діапазоні від 17 до 0 — "Good Evening". Верхня межа діапазону не враховується. Наприклад, число 6 входить до діапазону від 6 до 13.

value = int(input('Ведіть час в діапазоні від 0 год. до 23 год.: '))

if value >= 0 and value < 6:
    print('Good Night')
elif value >= 6 and value < 13:
    print('Good Morning')
elif value >= 13 and value < 17:
    print('Good Day')
elif value >= 17 and value <= 23:
    print('Good Evening')
else: 
    print('Не вірно вказаний діапазон.')