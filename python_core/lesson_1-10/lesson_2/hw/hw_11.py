print('''
      Завдання 11
Користувач вводить з клавіатури відстань, витрату бензину на 100 км і вартість трьох
видів бензину. Вивести на екран порівняльну таблицю з вартістю подорожі на різних
видах палива.
      ''')

distance = int(input('Ведіть дистанцію: '))
consumption =float(input('Ведіть розхід пального на 100 км: '))

a92 = float(input('Ведіть ціну a92 бензину: '))
a95 = float(input('Ведіть ціну a95 бензину: '))
s95 = float(input('Ведіть ціну s95 спиртового бензину: '))

distance = distance / 100 * consumption
a92 *= distance
a95 *= distance
s95 *= distance

print(f'Вартість поїздки на a92 = {a92}, a95 = {a95}, s95 = {s95}')
