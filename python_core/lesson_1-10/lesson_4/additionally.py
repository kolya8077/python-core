'''
1.Користувач вводить дві дати(день, місяць, рік у вигляді цілих чисел). Необхідно визначити і вивести кількість днів між цими двома датами. Для розрахунків врахувати високосні роки, а також коректне число днів у місяцях. (березень -31, вересень - 30, лютий 28 або 29)
'''

day1 = int(input("Введіть день першої дати: "))
month1 = int(input("Введіть місяць першої дати: "))
year1 = int(input("Введіть рік першої дати: "))

day2 = int(input("Введіть день другої дати: "))
month2 = int(input("Введіть місяць другої дати: "))
year2 = int(input("Введіть рік другої дати: "))

days1 = 0

if((year1 % 4==0) and (year1 % 100 !=0) or ( year1 % 400==0)):
    if (month1==1):
        days1 = day1
    elif(month1==2):
        days1=day1+31
    elif(month1==3):
        days1=day1+31+29
    elif(month1==4):
        days1=day1+31+29+31
    elif(month1==5):
        days1=day1+31+29+31+30
    elif(month1==6):
        days1=day1+31+29+31+30+31
    elif(month1==7):
        days1=day1+31+29+31+30+31+30
    elif(month1==8):
        days1=day1+31+29+31+30+31+31+31      
    elif(month1==9):
        days1=day1+31+29+31+30+31+31+30+31
    elif(month1==10):
        days1=day1+31+29+31+30+31+31+30+31+30
    elif(month1==11):
        days1=day1+31+29+31+30+31+31+30+31+30+31
    elif(month1==12):
        days1=day1+31+29+31+30+31+31+30+31+30+31+30
else:
    if (month1==1):
        days1 = day1
    elif(month1==2):
        days1=day1+31
    elif(month1==3):
        days1=day1+31+28
    elif(month1==4):
        days1=day1+31+28+31
    elif(month1==5):
        days1=day1+31+28+31+30
    elif(month1==6):
        days1=day1+31+28+31+30+31
    elif(month1==7):
        days1=day1+31+28+31+30+31+30
    elif(month1==8):
        days1=day1+31+28+31+30+31+31+31      
    elif(month1==9):
        days1=day1+31+28+31+30+31+31+30+31
    elif(month1==10):
        days1=day1+31+28+31+30+31+31+30+31+30
    elif(month1==11):
        days1=day1+31+28+31+30+31+31+30+31+30+31
    elif(month1==12):
        days1=day1+31+28+31+30+31+31+30+31+30+31+30

days2 = 0

if((year2 % 4==0) and (year2 % 100 !=0) or ( year2 % 400==0)):
    if (month2==1):
        days2 = day2
    elif(month2==2):
        days2=day2+31
    elif(month2==3):
        days2=day2+31+29
    elif(month2==4):
        days2=day2+31+29+31
    elif(month2==5):
        days2=day2+31+29+31+30
    elif(month2==6):
        days2=day2+31+29+31+30+31
    elif(month2==7):
        days2=day2+31+29+31+30+31+30
    elif(month2==8):
        days2=day2+31+29+31+30+31+31+31      
    elif(month2==9):
        days2=day2+31+29+31+30+31+31+30+31
    elif(month2==10):
        days2=day2+31+29+31+30+31+31+30+31+30
    elif(month2==11):
        days2=day2+31+29+31+30+31+31+30+31+30+31
    elif(month2==12):
        days2=day2+31+29+31+30+31+31+30+31+30+31+30
else:
    if (month2==1):
        days2 = day2
    elif(month2==2):
        days2=day2+31
    elif(month2==3):
        days2=day2+31+28
    elif(month2==4):
        days2=day2+31+28+31
    elif(month2==5):
        days2=day2+31+28+31+30
    elif(month2==6):
        days2=day2+31+28+31+30+31
    elif(month2==7):
        days2=day2+31+28+31+30+31+30
    elif(month2==8):
        days2=day2+31+28+31+30+31+31+31      
    elif(month2==9):
        days2=day2+31+28+31+30+31+31+30+31
    elif(month2==10):
        days2=day2+31+28+31+30+31+31+30+31+30
    elif(month2==11):
        days2=day2+31+28+31+30+31+31+30+31+30+31
    elif(month2==12):
        days2=day2+31+28+31+30+31+31+30+31+30+31+30

ollDay = days2 - days1

print(f"Кількість днів між датами: {ollDay} днів.")

'''
2.Дано два числа. Якщо вони різні, то поміняти іх місцями.
'''

number_1 = int(input("Введіть перше число: "))
number_2 = int(input("Введіть друге число: "))

if number_1 != number_2:
    replacement = number_1
    number_1 = number_2
    number_2 = replacement

    print("Число 1 після обміну: ", number_1)
    print("Число 2 після обміну: ", number_2)
else:
    print("Числа рівні, обмін не потрібний.")


'''
3.Розробити програму, що переводить значення температури в градусах по Цельсію в температуру по Фаренгейту та навпаки. Співвідношення між температурами визначається формулою: TF = TC *1.8 +32. Діалог с користувачем реалізувати через систему меню.
'''

print("Оберіть опцію:")
print("1. Перевести температуру з градусів Цельсія в градуси Фаренгейта")
print("2. Перевести температуру з градусів Фаренгейта в градуси Цельсія")

option = input("Ваш вибір (введіть 1 або 2): ")

if option == '1':
    tc = int(input("Введіть температуру в градусах Цельсія: "))
    tf = tc * 1.8 + 32
    print(f"Температура в градусах Фаренгейта: {tf}")
elif option == '2':
    tf = int(input("Введіть температуру в градусах Фаренгейта: "))
    tc = (tf - 32) * 5/9
    print(f"Температура в градусах Цельсія: {tc}")
else:
    print("Некоректний вибір.")

'''
4.Дано три числа. Якщо перше число більше третього, то поміняти іх місцями.
'''

number_1 = int(input("Введіть перше число: "))
number_2 = int(input("Введіть друге число: "))
number_3 = int(input("Введіть третє число: "))

if number_1 > number_3:
    replacement = number_1
    number_1 = number_3
    number_3 = replacement

    print("Число 1 після обміну: ", number_1)
    print("Число 3 після обміну: ", number_3)
else:
    print("Число 1 менше числа 3. Обмін не потрібний.")
