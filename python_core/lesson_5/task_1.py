
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


