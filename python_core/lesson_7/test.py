# while True:
    
#     day = int(input('Ведіть число: '))
#     month = int(input('Ведіть місяць: '))
#     year = int(input('Ведіть рік: '))
    
#     if month < 1 or month > 12:
#         print("Некоректний місяць. Введіть значення від 1 до 12.")
#         continue
    
#     month_one = month
#     name_month=''
    
#     if month == 1:
#         name_month = "January"
#     elif month == 2:
#         name_month = "February"
#     elif month == 3:
#         name_month = "March"
#     elif month == 4:
#         name_month = "April"
#     elif month == 5:
#         name_month = "May"
#     elif month == 6:
#         name_month = "June"
#     elif month == 7:
#         name_month = "July"
#     elif month == 8:
#         name_month = "August"
#     elif month == 9:
#         name_month = "September"
#     elif month == 10:
#         name_month = "October"
#     elif month == 11:
#         name_month = "November"
#     elif month == 12:
#         name_month = "December"
    
#     if month < 3:
#         month += 12
#         year -= 1
    
#     K = year % 100
#     J = year // 100
    
#     h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7

#     result = (h + 5) % 7
    
#     if((year % 4==0) and (year % 100 !=0) or ( year % 400==0)):
#         days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     else:
#         days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
#     days = days_in_month[month_one]
    
#     week_number = 0
    
#     for i in range(month_one):
#         week_number += days_in_month[i]

#     week_number = (week_number + day) // 7
    
#     print('\n', f'{name_month:^73}')
#     print()
    
#     arr = '№', 'Mo', 'To', 'We', 'Th', 'Fr', 'Sa', 'Su'
    
#     for i in range(8):
#         print('\t', arr[i], end='')
#     print()
    
#     i = 0
#     weekends = 0
    
#     if i == 0 and result != 0:
#         print('\t', week_number, end='')
#         for i in range(result):
#             print('\t', '_', end='',)
#         i += 1
#     for j in range(days_in_month[month_one]):
#         if j == 0:
#             j += 1
#         if i % 7 == 0:
#             week_number += 1   
#             i = 0
#             print('\n','\t', week_number, end='')
            
#         print('\t', j, end='')
#         i+=1
#         if (i % 6 ==0 or i % 7 == 0) and i != 0 and j != 0:
#             weekends += 1
#     print()
#     print('That month weekends is', weekends)
    
#     question = input('Бажаєте продовжити? YES = y, NO = n ')
    
#     if question == 'y':
#         continue
#     else:
#         break



n = 5

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1 or i == n // 2 or j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    