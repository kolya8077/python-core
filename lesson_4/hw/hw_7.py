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