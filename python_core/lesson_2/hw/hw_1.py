print('''
      Завдання 1
Користувач вводить з клавіатури грошову суму в гривнях і копійках (гривні і копійки
вводяться в різні змінні). Сума може бути введена як правильно (наприклад 19 грн 90
коп), так і неправильно (наприклад 22 грн 978 коп). Написати програму, яка,
використовуючи тільки лінійний алгоритм, здійснить коригування введення грошової
суми в правильну форму.
Наприклад, якщо користувач ввів 11 грн 150 коп, програма має вивести на екран суму 12
грн 50 коп.
      ''')

hrn = int(input('Кількість гривень: '))
cop = int(input('Кількість копійок: '))

hrn = hrn + cop // 100
cop = cop % 100
print(f'{hrn} грн {cop} коп')


