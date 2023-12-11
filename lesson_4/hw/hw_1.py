num1 = int(input('Сторона А: '))
num2 = int(input('Сторона Б: '))
num3 = int(input('Сторона В: '))

c = num3 ** 2
ab = num1 ** 2 + num2 ** 2

if c == ab:
  print('Трикутник прямокутній')
elif num1 == num2 == num3:
  print('Трикутник рівносторонній')
elif num1 == num2 or num2 == num3 or num3 == num2:
  print('Трикутник рівнобедрений')
else: 
  print('Трикутник різносторонній')