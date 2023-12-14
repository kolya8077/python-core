month = int(input('Введіть місяць (1-12): '))
year = int(input('Введіть рік (****): '))

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    if month == 2:
        if 1 <= day <= 28:
            print(f'Наступне число {day + 1}.{month}.{year}')
        else:
            print(f'Наступне число 1.{month + 1}.{year}')
    elif month in [1,3,5,7,8,10,12]:
        if 1 <= day <= 30 and 1 <= month <= 11:
            print(f'Наступне число {day + 1}.{month}.{year}')
        elif day == 31 and 1 <= month <= 11:
            print(f'Наступне число 1.{month + 1}.{year}')
        elif day == 31 and month == 12:
            print(f'Наступне число 01.01.{year + 1}')
    elif month in [2,4,6,9,11]:
        if 1 <= day <= 29 and 1 <= month <= 11:
            print(f'Наступне число {day + 1}.{month}.{year}')
        elif day == 30 and 1 <= month <= 11:
            print(f'Наступне число 1.{month + 1}.{year}')
        elif day == 30 and month == 12:
            print(f'Наступне число 01.01.{year + 1}')
    else:
        print(f'Наступне число 01.01.{year + 1}')
else:
    if month == 2:
        if 1 <= day <= 27:
            print(f'Наступне число {day + 1}.{month}.{year}')
        else:
            print(f'Наступне число 1.{month + 1}.{year}')
    elif month in [1,3,5,7,8,10,12]:
        if 1 <= day <= 30 and 1 <= month <= 11:
            print(f'Наступне число {day + 1}.{month}.{year}')
        elif day == 31 and 1 <= month <= 11:
            print(f'Наступне число 1.{month + 1}.{year}')
        elif day == 31 and month == 12:
            print(f'Наступне число 01.01.{year + 1}')
    elif month in [2,4,6,9,11]:
        if 1 <= day <= 29 and 1 <= month <= 11:
            print(f'Наступне число {day + 1}.{month}.{year}')
        elif day == 30 and 1 <= month <= 11:
            print(f'Наступне число 1.{month + 1}.{year}')
        elif day == 30 and month == 12:
            print(f'Наступне число 01.01.{year + 1}')
    else:
        print(f'Наступне число 01.01.{year + 1}')