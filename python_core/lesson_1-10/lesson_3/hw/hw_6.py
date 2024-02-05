num1 = int(input('Число 1: '))
num2 = int(input('Число 2: '))
num3 = int(input('Число 3: '))

num1 = num1 % 2 != 0
num2 = num2 % 2 != 0
num3 = num3 % 2 != 0

if num1 == num2 == num3 == True:
  print('Всі числа непарні')
else:
  print('Всі числа не непарні')