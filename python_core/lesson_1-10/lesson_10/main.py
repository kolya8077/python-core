# d\*\+d\•|•+d\•\+d\
import re

'''
Завдання 1:
Програма повинна знайти в текстовому файлі всі дробові числа. Дробовим вважається
число, в якого є значення після символу . (крапка) або , (кома) . 3.14....3,14
'''

mes = input('Вставте текст: ')

mes = re.findall(r'\d+\.\d+|\d+\,\d+', mes)
print(mes)

'''
Завдання 2:
Написати програму, яка зчитуватиме з клавіатури номер телефону
Зробити валідацію формату номеру телефона України: +38 (0**) ***-**-**
* - довільна цифра
(на додоткові 12 балів зробиті валідацію на всіх операторів)
'''

tel = input('Введіть номер телефону в форматі +38(0**)***-**-**: ')

vodofone = ['(050)', '(066)', '(099)', '(095)']
kyivstar = ['(096)', '(097)', '(098)', '(067)', '(068)']
life = ['(093)', '(063)', '(073)']

audit = re.findall(r'\(\d{3}\)', tel)

tel_validated = re.search(r'\+\d{2}\(\d{3}\)\d{3}-\d{2}-\d{2}', tel)
if tel_validated:
    print("Номер телефону відповідає формату України")

    for i in vodofone:
        if i in audit:
            print("Ваш оператор: Vodafone")
    for j in kyivstar:
        if j in audit:
            print("Ваш оператор: kyivstar")
    for n in life:
        if n in audit:
            print("Ваш оператор: life")
    print('Ваш номер телефона ',tel)
else:
    print("Номер телефону не відповідає формату України")
    
mes = 'Searches the string for a specified value and returns the position of where it was found (python snippets)'

print(re.find('the', mes))

