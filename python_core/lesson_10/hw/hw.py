'''
Завдання 3:
Користувач вводить email та пароль. Написати програму для їх валідації (перевірки на коректність). 
Правила для адреси: 
1. ім'я може містити лише латинські літери, цифри, та символи ‘.’ ‘_’ ‘-‘
2. мінімальний розмір імені - 4 символа
3. обов'язкова наявність @ після імені
4. назва доменту може включати лише алфавітно-числові символи та не менше 2-х 
символів
5. всередині назви домену обов'язкова наявність .(крапки)
Правила для паролю: 
1. пароль може містити латинські літери, цифри, _(підчеркування) та -(дефіс)
2. мінімальний розмір - 6 символів
3. обов'язкова наявність хоча б одного символу літери, як великої так і маленької, цифри та іншого символу (дефіс або підчеркування)
'''

import re
import getpass

email = input("Введіть email: ")
password = getpass.getpass("Введіть пароль: ")
# password = input("Введіть пароль: ")


validate_email = re.match(r'^[a-zA-Z0-9._-]{4,}@[a-zA-Z0-9-]{2,}\.[a-zA-Z0-9.-]+$', email)
validate_password = re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9-_]).{6,}$', password)

if validate_email and validate_password:
    print("Введені дані коректні.")
else:
    print("Введені дані некоректні.")



