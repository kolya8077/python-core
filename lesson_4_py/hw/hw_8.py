num1 = int(input('Оцінка 1: '))
num2 = int(input('Оцінка 2: '))
num3 = int(input('Оцінка 3: '))

result = (num1 + num2 + num3) / 3

print(f'{result:.1f}')
if 2 <= result <= 2.5:
  print('BAD')
elif 2.5 < result <= 3.3:
  print('SO-SO')
elif 3.3 < result <= 4.2:
  print('GOOD')
elif 4.2 < result <= 5.0:
  print('EXCELLENT')